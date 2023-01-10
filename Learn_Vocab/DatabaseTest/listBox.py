from tkinter import *

def delete():
    listBox.delete(ANCHOR)
    result=listBox.curselection()
    
    for item in reversed(result):
        listBox.delete(item)
    label1.config(text="")

def select():
    result=listBox.curselection()
    textLab=''
    for item in result:
        textLab+=str(listBox.get(item))+ " "
    label1.config(text=textLab)
    

main=Tk()
main.title("BoxList Testing")

frame=Frame(main)
scroll=Scrollbar(frame, orient=VERTICAL)

listBox=Listbox(frame, 
                width=50, 
                bd=5, 
                yscrollcommand=scroll.set,
                selectmode=MULTIPLE,
                selectbackground="pink",
                selectborderwidth=5,
                foreground="black")
scroll.config(command=listBox.yview)
scroll.pack(side=RIGHT, fill=Y)

for index in range(0,100):
    listBox.insert(END, str(index))
listBox.pack()

frame.pack()





button1=Button(main,text="Delete", command=lambda: delete())
button1.pack()
button2=Button(main,text="Select", command=lambda: select())
button2.pack() 

global label1
label1=Label(main,text="")
label1.pack()

main.mainloop()