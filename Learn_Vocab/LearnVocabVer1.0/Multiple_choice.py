from tkinter import *

def setup():
    global root
    global eat
    root=Tk()
    root.title("Multiple Choice 1.0")
    eat = StringVar()
    eat.set("Apple")
    create_answer()
    but=Button(root, text= "click", command=lambda: clickme(eat.get())).pack()
    root.mainloop()

def clickme(temp):
    ann=Label(root, text=temp).pack()

def create_answer():
    global Fruits
    Fruits=[
        ("Apple","Apple"),
        ("Orange","Orange"),
        ("Banana","Banana"),
        ("Pinapple","Pinapple")
    ]
    for fruit, val in Fruits:
        Radiobutton(root, text=fruit, variable=eat, value=val).pack(anchor=W)


setup()
