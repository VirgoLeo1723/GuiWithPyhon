from random import choice, random, randrange
from tkinter import *
from tkinter.font import BOLD
from typing import get_origin
from PIL import ImageTk,Image
from string import *
from tkinter import messagebox

def setup():
    global new_word
    global kind
    global mean
    global root
    global frame2
    global frame3
    root=Tk()
    root.title("Learn Vocab 1.0")
    root.iconbitmap('favicon.ico')

    frame1=LabelFrame(root, pady=50, padx=50, bg="#FDF5CA")
    frame1.grid(row=0, column=0, pady=50, padx=50)


    intro=Label(frame1,text="THIS APPLICATION HAS 2 OPTION", width=40,pady=10, bg="#FDF5CA")
    but_new=Button(frame1,text="Add New Vocab",width=10, pady=10, padx=10, bg="#F2BB7B", command=lambda: New())
    but_learn=Button(frame1,text="Learning Mode", width=10, padx=10, pady=10, bg="#F2BB7B", command=lambda: Learn())

    intro.grid(row=0, column=0, columnspan=2)
    but_new.grid(row=1, column=0)
    but_learn.grid(row=1, column=1)

    root.mainloop()

def Update_list(var_list):
    f2=open("Vocab.txt","rb")
    while True:
        st=f2.readline().decode("utf8")
        var_list.append(st)
        if not st: break


def New_reset():
    global frame2
    global kind
    global mean
    global word
    word.delete(0,END)
    kind.delete(0,END)
    mean.delete(0,END)


def New_process(temp1, temp2, temp3):
    global frame2
    global vocab_dict
    f1=open("Vocab.txt","ab")
    temp_check=temp1+":"+temp3+" ("+temp2+")\n"
    #print(temp_check)
    ann=Label(frame2, text="" + temp1,bg="#FDF5CA")
    ann.grid(row=2, column=3)
    ann.grid_forget()
    if not(temp_check in vocab_dict):
        ann=Label(frame2, text="ADDED " + temp1,bg="#FDF5CA",width=15)
        ann.grid(row=2, column=3)
        st=(str(temp1)+":"+str(temp3)+" ("+str(temp2)+")\n").encode("utf8")
        f1.write(st)
    else: 
        ann=Label(frame2,text="AVAILABLE",bg="#FDF5CA", width=15)
        ann.grid(row=2, column=3)

    New_reset()
    
    f1.close()


def New():
    global root
    global kind
    global mean
    global word
    global frame2
    global frame3
    global vocab_dict
    vocab_dict=[]
    Update_list(vocab_dict)
    #print(vocab_dict)
    try:
        frame3.grid_forget()
    except NameError as er:
        pass
    frame2=LabelFrame(root, pady=50, padx=50, bg="#FDF5CA")
    frame2.grid(row=0, column=1, pady=50, padx=50)
    
    intro_new=Label(frame2,text="Enter in oder like this: word, kind of word, definition", width=50 ,pady=10, padx=10,bg="#FDF5CA")
    word=Entry(frame2, border=1, width=10)
    kind=Entry(frame2, border=1, width=5)
    mean=Entry(frame2, border=1, width=20)
    but_add=Button(frame2, text="ADD", padx=10, pady=10, width=10, command=lambda: New_process(word.get(), kind.get(), mean.get()), bg="#F2BB7B")
    intro_new.grid(row=0, column=0, columnspan=4)
    word.grid(row=1, column=0)
    kind.grid(row=1, column=1)
    mean.grid(row=1, column=2)
    but_add.grid(row=1,column=3)

def reset_frame(frame):
    frame.grid_forget()

def set_frame4():
    global remember
    frame4=LabelFrame(root, pady=10, padx=10, bg="#FDF5CA")
    frame4.grid(row=0, column=1, pady=50, padx=50)
    intro=Label(frame4,text="TRY TO REMEMBER THESE WORD", width=50, bg="#FFDFAF", pady=10)
    intro.grid(row=0, column=0, columnspan=2)
    index=1
    for mean in remember:
        temp=Label(frame4,text=mean+" : "+remember[mean], width=50,bg="#FDF5CA", anchor=W)
        temp.grid(row=index, column=0)
        index+=1
    but_reset=Button(frame4,text="CLOSE", command=lambda: reset_frame(frame4),bg="#F2BB7B", width=10)
    but_reset.grid(row=index+2, column=1)


def pass_ques():
    global num_word
    global word_list
    global group
    global time_each_word
    global vocal_dict
    global used_vocab
    global remember
    #print(len(used_vocab))
    #print(len(word_list))
    
    time_each_word=2
    if num_word>0:
        word=choice(word_list)
        if word in used_vocab: pass_ques()
        elif word!="":
            group=(word.split(":"))
            group[1]=group[1][:len(group[1])-1]
            Def=Label(frame3, text=group[1], width=30, pady=10, padx=10,bg="#FDF5CA")
            Def.grid(row=2,column=0)
            used_vocab.append(word)
            num_word-=1 
    else: 
        mess=messagebox.askyesno("Message", "Do you want to play again ???")
        if mess==0:
            frame3.grid_forget()
            set_frame4()
        else: 
            frame3.grid_forget()
            Learn()
    

def Learn_check():
    global answer2
    global group
    global num_word
    global time_each_word
    global remember
    ans=answer2.get()
    answer2.delete(0,END)
    if ans==group[0] : 
        ann=Label(frame3,text="CORRECT",bg="#FDF5CA")
        ann.grid(row=3, column=3)
        pass_ques()
    elif time_each_word>0: 
        ann=Label(frame3,text="TRY AGAIN",bg="#FDF5CA")
        ann.grid(row=3, column=3)
        time_each_word-=1
    else: 
        ann=messagebox.askyesno("End of allowed turn", "Do you want to pass ???")
        if ann==0: time_each_word=3
        else: 
            remember.update({group[1]: group[0]})
            pass_ques()

def Learn_process(temp):
    global frame3
    global word_list
    global answer2
    global group
    global num_word
    global user_point
    global time_each_word
    time_each_word=3

    Def=Label(frame3, text="Definition", width=10, pady=10, padx=10,bg="#FDF5CA")
    Def.grid(row=2,column=0)
    answer2=Entry(frame3, border=1, width=10)
    but_sub=Button(frame3, text="SUBMIT",bg="#F2BB7B", command=lambda: Learn_check())
    answer2.grid(row=2, column=1)
    but_sub.grid(row=2, column=3)


    if temp=="all" or int(temp)>len(word_list): num_word=len(word_list)-3
    elif temp=="pass": pass_ques()
    else: num_word=int(temp)
    pass_ques()

def Learn():
    global frame2
    global frame3
    global word_list
    global used_vocab
    global remember
    remember={}
    used_vocab=[]
    try:
        frame2.grid_forget()
    except NameError as er:
        pass

    frame3=LabelFrame(root, pady=50, padx=50, bg="#FDF5CA")
    frame3.grid(row=0, column=1, pady=50, padx=50)
    word_list=[]
    Update_list(word_list)
  
    Title=Label(frame3, text="You will have 3 times to guess the word", width=50, pady=10, padx=10, bg="#FFDFAF")
    intro_learn1=Label(frame3, text="How many word you want to learn? (all/x)",width= 30, pady=10, padx=10,bg="#FDF5CA")
    answer1=Entry(frame3, border=1, width=5)
    but_ready=Button(frame3, text="Go", command=lambda: Learn_process(answer1.get()), bg="#F2BB7B", width=6)
    #but_ready.bind("<Enter>",Learn_process(answer1.get()))
    Title.grid(row=0, columnspan=4, column=0)
    intro_learn1.grid(row=1, column=0)
    answer1.grid(row=1, column=1)
    but_ready.grid(row=1, column=3)



setup()