from tkinter import *

root=Tk()
root.title("Frame_Work")

frame1=LabelFrame(root, padx=50, pady=50) #padx, pady in this line: khoảng cách từ viền đến phần tử
frame1.grid(row=0, column=0,pady=5, padx=5) #padx, pady in this line: khoảng cách từ viên đến các root
frame2=LabelFrame(root, padx=50, pady=50) 
frame2.grid(row=0, column=1,pady=5, padx=5)

but1=Button(frame1, text="click", padx=5, pady=5)
but1.grid(row=1, column=1)
but2=Button(frame2, text="click", padx=5, pady=5)
but2.grid(row=1, column=1)

root.mainloop()