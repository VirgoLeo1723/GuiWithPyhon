from tkinter import *
from tkinter import ttk

main=Tk()
main.title("Tabs Testing")
main.geometry("500x500")
notebook=ttk.Notebook(main)
notebook.pack()

def goto():
    #notebook.add(tab2, text="Tab2")
    notebook.select(tab2)
    tab2.config(pady=200, padx=200)
    tab1.config(pady=200, padx=200)
    
def backto():
    notebook.hide(1)
    tab2.config(pady=200, padx=200)
    tab1.config(pady=200, padx=200)


global tab1
global tab2
tab1=Canvas(notebook, bg="pink")
tab2=Canvas(notebook, bg="lightblue")

tab1.pack(fill=BOTH, expand=1)
tab2.pack(fill=BOTH, expand=1)

notebook.add(tab1, text="Tab1")
notebook.add(tab2, text="Tab2")


button1=Button(tab1,text="Open Tab2", command=goto).pack()
button2=Button(tab2,text="Back Tab1", command=backto).pack()

notebook.hide(tab2)
main.mainloop()