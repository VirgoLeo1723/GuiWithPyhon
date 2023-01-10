from tkinter import *
from tkinter import colorchooser
main=Tk()
main.title("Colorpicker Testing")

def color():
    color=colorchooser.askcolor()
    ann=Label(main,text=f"color= {color[1]}",bg=color[1]).pack()


colorPickButton=Button(main, text="Pick a color", command=color).pack()

main.mainloop()