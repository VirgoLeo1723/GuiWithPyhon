from tkinter import *
from tkinter import ttk
main=Tk()
main.title("Binding  Testing")

def clicker(event):
    label=Label(main, text="Clicked " +str(event))
    label.pack()
def clicker2(event):
    print(event.char)
    if event.char=='/n':
        label=Label(main, text="Clicked " +str(combo.get()))
        label.pack()

button=Button(main, text="Binding")
button.bind("<Key>", clicker)
button.bind("<Button-1>", clicker)
button.pack()

option=[
    "Monday",
    "Tuesday",
    "wednesday",
    "Thursday"
]
click=StringVar()
click.set(option[0])

drop=OptionMenu(main, click, *option, command=clicker)
drop.pack()

combo=ttk.Combobox(main, value=option)
combo.current(0)
combo.bind("<<ComboboxSelected>>",clicker2)
combo.bind("<Key>",clicker2)
combo.pack()
main.mainloop()