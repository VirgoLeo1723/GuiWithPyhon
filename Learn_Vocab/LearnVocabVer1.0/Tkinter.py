from tkinter import *

root =Tk()

e=Entry(root,width=50)
e.grid(row=1, column=0)
e.insert(0,"Enter word: ")

def myClick():
    print(f"Input: {e.get()}")
    ann = Label(root, text="New word: " + e.get())
    ann.grid(row=2, column=1)



myLabel = Label(root ,text="Learn Vocab 1.0" )
button  = Button(root, text="Submit", command=myClick, fg="#FFC2B4", bg="#194350", border=0)

myLabel.grid(row=0,column=0)
button.grid(row=1, column=1)

#myLabel.pack()

root.mainloop()