from tkinter import *
from tkinter import colorchooser

def changeText():
    temp=subEntry.get()
    color=colorchooser.askcolor()
    label.config(text=temp, bg=color[1])
    button.config(text=temp)

main=Tk()
main.title("Config Testing")
main.geometry("400x400")

subEntry=Entry(main)
subEntry.pack()

global label
global button
global color
label=Label(main,text="")
button=Button(main,text="Entry", command=lambda:changeText())
label.pack()
button.pack()


main.mainloop()