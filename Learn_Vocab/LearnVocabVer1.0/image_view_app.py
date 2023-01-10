from tkinter import *
from PIL import ImageTk,Image
from string import *
from tkinter import messagebox

root=Tk()
root.title("Guess word by image 1.0")
root.iconbitmap('d:/Study/Python/Learn_Vocab/Image/favicon.ico')

img1=ImageTk.PhotoImage(Image.open('d:/Study/Python/Learn_Vocab/Image/cat.png'))
img2=ImageTk.PhotoImage(Image.open('d:/Study/Python/Learn_Vocab/Image/dog.jpg'))
img3=ImageTk.PhotoImage(Image.open('d:/Study/Python/Learn_Vocab/Image/bird.png'))
img4=ImageTk.PhotoImage(Image.open('d:/Study/Python/Learn_Vocab/Image/rabbit.jpg'))
img_list=[img1,img2, img3, img4]
dict_img={
    img1:"cat",
    img2:"dog",
    img3:"bird",
    img4:"rabbit"
}

show_img=Label(image=img1)
show_img.grid(row=0, column=0, columnspan=4)
user_point=1


def Next_qe():
    global show_img
    global Pass
    global num_img

    if (num_img<len(img_list)-1): num_img+=1
    else: num_img=0

    show_img.grid_forget()
    show_img=Label(image=img_list[num_img])
    show_img.grid(row=0, column=0, columnspan=4)
    Pass=Button(root, text="Pass", padx=40, pady=10, command=lambda: Next_qe(num_img))
    Status=Label(root, text="Question " +str(num_img+1) +" of "+str(len(img_list)),anchor=E)
    Status.grid(row=2,column=0, columnspan=4 ,sticky=W+E)
    
def Ques():
    global user_point
    temp=messagebox.askyesno("Message", "Do you want to play again ???")
    if temp==0:
        root.quit()
    else: 
        user_point=0
        Point=Label(root, text="Point", padx=40, pady=10, bg="#2D2424", fg="#E0C097")
        Point.grid(row=1, column=3)

def check(st):
    global num_img
    global Point
    global user_point

    if st==dict_img[img_list[num_img]] and user_point<=len(img_list): 
        Point=Label(root, text="Point: " + str(user_point), padx=40, pady=10, bg="#2D2424", fg="#E0C097")   
        Point.grid(row=1, column=3) 
        user_point+=1
        ann=Label(root,text="Hurayyyyy !!!!!!!!!", width=20, padx=5, pady=5)
        ann.grid(row=0, column=0)
    else:
        ann=Label(root,text="Try Again !!!!!!!!!!!!", width=20, padx=5, pady=5)
        ann.grid(row=0, column=0)
        Answer.delete(0, END)


    if (user_point>len(img_list)):
        ann=Label(root,text="You Win !!!!!!!!!",width=20, padx=5, pady=5)
        ann.grid(row=0, column=0)
        Ques()

num_img=0
Answer=Entry(root,width=40, border=4)
Submit=Button(root, text="SUBMIT", pady=10, padx=40, command=lambda: check(Answer.get()))
Pass=Button(root, text="Pass", padx=40, pady=10, command=lambda: Next_qe())
Point=Label(root, text="Point", padx=40, pady=10, bg="#2D2424", fg="#E0C097")
Status=Label(root, text="Question 1 of "+str(len(img_list)), anchor=E)


Answer.grid(column=0, row=1, padx=0, pady=20)
Submit.grid(column=1, row=1)
Pass.grid(row=1, column=2)
Point.grid(row=1, column=3)
Status.grid(row=2,column=0, columnspan=4, sticky=W+E)

root.mainloop()

