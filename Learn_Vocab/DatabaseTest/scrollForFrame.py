from tkinter import * 

main=Tk()
main.title("Scrollbar testing")

frame=Frame(main)
canvas=Canvas(frame)
canvas.pack(side=LEFT, fill=BOTH)

scroll=Scrollbar(main, orient=VERTICAL)
canvas.config(yscrollcommand=scroll.set)

scroll.config(command=canvas.yview)
scroll.pack(side=RIGHT, fill=Y)
frame.pack()

for index in range(0,99):
    label=Label(canvas,text=str(index))
    label.pack()


main.mainloop()