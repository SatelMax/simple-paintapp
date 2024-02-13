from tkinter import *
from tkinter import colorchooser

gui = Tk()
gui.title("Paint App")
gui.geometry("600x580+270+0")

brush_color = "black"
brush_type = StringVar(name="Type")
brush_type.set("round")

def paint(e):
    x1, y1 = e.x - 1, e.y - 1
    x2, y2 = e.x, e.y
    brush = brush_type.get()
    my_canvas.create_line(x1, y1, x2, y2, fill=brush_color, width=10, capstyle=brush)

def change_brush_color():
    global brush_color
    brush_color = colorchooser.askcolor(color=brush_color)[1]

def erase():
    global brush_color
    brush_color = "white"

def clear_screen():
    my_canvas.delete(ALL)

my_canvas = Canvas(gui, width=465, height=480, bg="white", cursor='circle')
my_canvas.pack(side="right", fill="both")
my_canvas.bind("<B1-Motion>", paint)

tools = LabelFrame(gui, text="Color Set", font=("Helvetica", 16, "bold"), bg="lightblue")
tools.pack(side="left", fill="both", expand="yes")

brush_color_button = Button(
    tools, text="Brush Color", font=("Sans", 10, "bold"), width=12, border=7, background="lightgreen", 
    activebackground="red", activeforeground="white", command=change_brush_color
)
brush_color_button.place(x=10, y=10)

brush_type_label = Label(
    tools, text="Brush Type", relief="raised", width=11, font=("Sans", 10, "bold")
)

brush_type_menu = OptionMenu(tools, brush_type, "round", "butt", "projecting")
brush_type_menu.config(font=("Sans", 10, "bold"), width=9, border=7, background="lightgreen", activebackground="red", activeforeground="white")
brush_type_menu.place(x=10, y=50)

erase = Button(tools, text="Eraser", font=("Sans", 10, "bold"), width=12, border=7, background="lightgreen", 
    activebackground="red", activeforeground="white", command=erase)
erase.place(x=10, y=94)

clear_screen = Button(
    tools, text="Clear Screen", font=("Sans", 10, "bold"), width=12, border=7, background="lightgreen", 
    activebackground="red", activeforeground="white", command=clear_screen
)
clear_screen.place(x=10, y=136)

gui.mainloop()
