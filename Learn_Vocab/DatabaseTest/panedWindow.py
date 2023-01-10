from tkinter import *

root=Tk()
root.title("panedWindow Testing")

panel1_1=PanedWindow(root, bd=4, relief="flat",bg="red")
panel1_1.pack(fill=BOTH, expand=1)

leftLabel=Label(panel1_1, text="Left Panel")
panel1_1.add(leftLabel)
leftButton=Button(panel1_1, text="Left")
leftButton.grid(row=10, column=10)

panel1_2=PanedWindow(panel1_1, orient=VERTICAL, bd=4, relief="raised", bg="blue")
panel1_1.add(panel1_2)

topLabel=Label(panel1_2, text="Top Panel")
panel1_2.add(topLabel)

bottomLabel=Label(panel1_2, text="Bottom Panel")
panel1_2.add(bottomLabel)

addLabel=Label(panel1_2, text="Add Panel")
panel1_2.add(addLabel)


root.mainloop()