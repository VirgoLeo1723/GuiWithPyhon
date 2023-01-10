from tkinter import *
from string import *

root=Tk()
root.title("CALCULATOR 1.0")
e=Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, pady=10, padx=20)
#e.insert(0,"")

def process(string):
    num=["1","2","3","4","5","6","7","8","9","0"]
    clear=["CE","AC","C"]
    option=["+","-","*","/"]
    str=e.get()
    if string in num:
        if string=="0":
            if str!="" and not(str[len(str)-1] in option): e.insert(END,string)
            else: pass
        else:e.insert(END,string)
    elif string in clear:
        if string=="CE": e.delete(len(e.get())-1,END)
        elif string=="AC": e.delete(0,END)
        else: pass
    elif string in option:
        e.insert(END," "+string+" ")
    else: result(e.get())
    
def result(st):
    st=st.split(" ")
    print(st)
    temp_r=0
    while "*" in st or "/" in st:
        if "*" in st: 
            pos1=st.index("*")
            temp1=float(st[pos1-1])*float(st[pos1+1])
            st[pos1-1]=str(temp1)
            st.pop(pos1+1)
            st.pop(pos1)
            print(st)
        if "/" in st:
            pos2=st.index("/")
            temp1=float(st[pos2-1])/float(st[pos2+1])
            st[pos2-1]=str(temp1)
            st.pop(pos2+1)
            st.pop(pos2)
            print(st)
    
    while "+" in st or "-" in st:
        if "+" in st: 
            pos1=st.index("+")
            temp1=float(st[pos1-1])+float(st[pos1+1])
            st[pos1-1]=str(temp1)
            st.pop(pos1+1)
            st.pop(pos1)
            print(st)
        if "-" in st:
            pos2=st.index("-")
            temp1=float(st[pos2-1])-float(st[pos2+1])
            st[pos2-1]=str(temp1)
            st.pop(pos2+1)
            st.pop(pos2)
            print(st)
    if len(st)==1: temp_r+=float(st[0])
    e.delete(0,END)
    e.insert(0,str(temp_r))

but_del_crt=Button(root, text="CE", padx=35, pady=20 , command=lambda: process("CE"))
but_del_all=Button(root, text="AC", padx=35, pady=20 , command=lambda: process("AC"))
but_del_1=Button(root, text="C", padx=39,pady=20 , command=lambda: process("C"))
but1=Button(root, text="1", padx=40, pady=20 , command=lambda: process("1"))
but2=Button(root, text="2", padx=40, pady=20 , command=lambda: process("2"))
but3=Button(root, text="3", padx=40, pady=20 , command=lambda: process("3"))
but4=Button(root, text="4", padx=40, pady=20 , command=lambda: process("4"))
but5=Button(root, text="5", padx=40, pady=20 , command=lambda: process("5"))
but6=Button(root, text="6", padx=40, pady=20 , command=lambda: process("6"))
but7=Button(root, text="7", padx=40, pady=20 , command=lambda: process("7"))
but8=Button(root, text="8", padx=40, pady=20 , command=lambda: process("8"))
but9=Button(root, text="9", padx=40, pady=20 , command=lambda: process("9"))
but0=Button(root, text="0", padx=40, pady=20 , command=lambda: process("0"))
but_plus=Button(root, text="+", padx=40,  pady=20 , command=lambda: process("+"))
but_minus=Button(root, text="-", padx=40,  pady=20 , command=lambda: process("-"))
but_multi=Button(root, text="*", padx=40,  pady=20 , command=lambda: process("*"))
but_div=Button(root, text="/", padx=40,  pady=20 , command=lambda: process("/"))
but_equal=Button(root, text="=", width=40, pady=20 , command=lambda: process("="))

but_del_crt.grid(row=1,column=0)
but_del_all.grid(row=1,column=1)
but_del_1.grid(row=1,column=2)
but1.grid(row=2, column=0)
but2.grid(row=2, column=1)
but3.grid(row=2, column=2)
but4.grid(row=3, column=0)
but5.grid(row=3, column=1)
but6.grid(row=3, column=2)
but7.grid(row=4, column=0)
but8.grid(row=4, column=1)
but9.grid(row=4, column=2)
but0.grid(row=5, column=0)
but_plus.grid(row=1, column=3)
but_minus.grid(row=2, column=3)
but_multi.grid(row=3, column=3)
but_div.grid(row=4, column=3)
but_equal.grid(row=5, column=1, columnspan=3)

root.mainloop()