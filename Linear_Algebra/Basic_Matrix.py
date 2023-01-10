
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from numpy import array, ulonglong
from sympy.core.facts import _base_fact
from matrix_module import matrix_operator as mtr



COLOR_1="#FF7B54"
COLOR_2="#FFB26B"
COLOR_3="#FFD56B"
COLOR_4="#939B62"
format=int


B_dis=0

root=Tk()
root.title("Linear Algebra")
root.geometry("800x400")
root.resizable(0,0)

def clear():
    global matrixA
    global matrixB
    matrixA=Frame(root)
    matrixB=Frame(root)
    matrixA.config(bg=COLOR_4)
    matrixB.config(bg=COLOR_3)
    matrixA.place(relwidth=0.3, relheight=1, relx=0.4)
    matrixB.place(relwidth=0.3, relheight=1, relx=0.7)
def print_result(result):
    global format
    if temp=="Echelon Form": format=float
    result=array(result.tolist(), dtype=format)
    x=0.1
    y=0.6
    for row in range(0,result.shape[0]):
        for col in range(0,result.shape[1]):
            entry=Entry(inf_frame)
            entry.place(relwidth=0.08, relx=x, rely=y)
            entry.insert(0,str(result[row][col]))
            entry.config(relief="flat")
            x+=0.12
        y+=0.07
        x=0.1
def submit():
    A_value=[]
    B_value=[]
    result=[]
    for i in range(0, A_row):
        row=[]
        for j in range(0, A_col):
            row.append(int(A_entry[i][j].get()))
        A_value.append(row)
    A_check=1
    if B_dis==0:
        for i in range(0, B_row):
            row=[]
            for j in range(0, B_col):
                row.append(int(B_entry[i][j].get()))
            B_value.append(row)
        B_check=1
    if temp=="Add":
        if A_row!=B_row or A_col!=B_col: messagebox.showerror("ERROR","Different size")
        else: result=mtr.plus(mtr.pow(A_value,int(powerA_entry.get())),mtr.pow(B_value,int(powerB_entry.get())))
    if temp=="Multiply":
        if A_col!=B_row: messagebox.showerror("ERROR","Different size")
        else: result=mtr.multi(mtr.pow(A_value,int(powerA_entry.get())),mtr.pow(B_value,int(powerB_entry.get())))
    if temp=="Power": result=mtr.pow(A_value,int(powerA_entry.get()))
    if temp=="Transpose": result=mtr.trans(mtr.pow(A_value,int(powerA_entry.get())))
    if temp=="Echelon Form": result=mtr.eche_form(mtr.pow(A_value,int(powerA_entry.get())))
    print_result(result)
def process():    
    clear()
    global A_check
    global B_check
    global A_value
    global B_value
    global A_entry
    global B_entry
    global A_col
    global A_row
    global B_col
    global B_row
    global temp
    A_check=0
    B_check=0
    A_entry=[]
    B_entry=[]
    A_value=[]
    B_value=[]
   
    # Matrix A
    x=0.1
    y=0.1
    A_col=int(sizeA_entry_col.get())
    A_row=int(sizeA_entry_row.get())
    for i in range(0, A_row): #0->2 
        row=[]
        for j in range(0, A_col): #0->1
            entry=Entry(matrixA)
            entry.place(relwidth=0.1, relx=x, rely=y)
            entry.config(relief="flat")
            row.append(entry)
            x+=0.15
        A_entry.append(row)
        y+=0.07
        x=0.1
    
    # Matrix B
    x=0.1
    y=0.1
    if B_dis==0:
        B_col=int(sizeB_entry_col.get())
        B_row=int(sizeB_entry_row.get())
    
        for i in range(0, B_row):
            row=[]
            for j in range(0, B_col):
                entry=Entry(matrixB)
                entry.place(relwidth=0.1, relx=x, rely=y)
                entry.config(relief="flat")
                row.append(entry)
                x+=0.15
            B_entry.append(row)
            y+=0.07
            x=0.1
            
    temp=box_list.get()
    if temp=="Add":
        if A_row!=B_row or A_col!=B_col: messagebox.showerror("ERROR","Different size")
    if temp=="Multiply":
        if A_col!=B_row: messagebox.showerror("ERROR","Different size")

    
def pre_process(event):
    global B_dis
    temp=box_list.get()
    clear()
    if temp in ["Echelon Form","Power","Transpose"]: 
        sizeA_entry_row.delete(0, END)
        sizeA_entry_col.delete(0, END)
        sizeB_entry_row.delete(0, END)
        sizeB_entry_col.delete(0, END)
        sizeB_entry_row.config(state="disabled")
        sizeB_entry_col.config(state="disabled")
        sizeB_label.config(state="disabled")
        powerB_label.config(state="disabled")
        powerB_entry.config(state="disabled")
        
        B_dis=1
    else:
        sizeB_entry_row.config(state="normal")
        sizeB_entry_col.config(state="normal")
        sizeB_label.config(state="normal")
        powerB_label.config(state="normal")
        powerB_entry.config(state="normal")
        B_dis=0
func_list=["Add","Multiply","Echelon Form","Power","Transpose"]

global matrixA
global matrixB
root_canvas=Canvas(root)
inf_frame=Frame(root)
matrixA=Frame(root)
matrixB=Frame(root)
select_label=Label(inf_frame, text="Select Function")
box_list=ttk.Combobox(inf_frame, values= func_list)
sizeA_label=Label(inf_frame, text="Size of Matrix A ")
sizeB_label=Label(inf_frame, text="Size of Matrix B ")
sizeB_entry_row=Entry(inf_frame)
sizeA_entry_row=Entry(inf_frame)
sizeB_entry_col=Entry(inf_frame)
sizeA_entry_col=Entry(inf_frame)
powerA_label=Label(inf_frame, text="Power")
powerB_label=Label(inf_frame, text="Power")
powerA_entry=Entry(inf_frame)
powerB_entry=Entry(inf_frame)
input_button=Button(inf_frame, text="Enter Value", command=process)
result_button=Button(inf_frame, text="Show result", command=submit)
result_label=Label(inf_frame, text="Result of equation")

box_list.set(func_list[0])
box_list.bind("<<ComboboxSelected>>", pre_process)

inf_frame.config(bg=COLOR_3)
matrixA.config(bg=COLOR_4)
matrixB.config(bg=COLOR_3)
select_label.config(fg=COLOR_4, bg=COLOR_3)
sizeA_label.config(bg=COLOR_4, fg=COLOR_3)
sizeB_label.config(bg=COLOR_4, fg=COLOR_3)
powerA_label.config(bg=COLOR_4, fg=COLOR_3)
powerB_label.config(bg=COLOR_4, fg=COLOR_3)
sizeA_entry_row.config(relief="flat")
sizeA_entry_col.config(relief="flat")
sizeB_entry_row.config(relief="flat")
sizeB_entry_col.config(relief="flat")
powerA_entry.config(relief="flat")
powerB_entry.config(relief="flat")
powerA_entry.insert(0,"1")
powerB_entry.insert(0,"1")
input_button.config(bg=COLOR_2, fg=COLOR_1, relief=FLAT)
result_button.config(bg=COLOR_2, fg=COLOR_1, relief=FLAT)
result_label.config(fg=COLOR_4, bg=COLOR_3)

inf_frame.place(relwidth=0.4, relheight=1)
matrixA.place(relwidth=0.3, relheight=1, relx=0.4)
matrixB.place(relwidth=0.3, relheight=1, relx=0.7)
select_label.place(relwidth=0.4, relx=0.1, rely=0.1)
box_list.place(relwidth=0.4, relx=0.56, rely=0.1)
sizeA_label.place(relwidth=0.4, relx=0.05, rely=0.2)
sizeB_label.place(relwidth=0.4, relx=0.05, rely=0.3)
sizeA_entry_row.place(relwidth=0.08, relx=0.46, rely=0.2)
sizeA_entry_col.place(relwidth=0.08, relx=0.56, rely=0.2)
sizeB_entry_row.place(relwidth=0.08, relx=0.46, rely=0.3)
sizeB_entry_col.place(relwidth=0.08, relx=0.56, rely=0.3)
powerA_label.place(relwidth=0.2, relx=0.66, rely=0.2)
powerB_label.place(relwidth=0.2, relx=0.66, rely=0.3)
powerA_entry.place(relwidth=0.08, relx=0.87, rely=0.2)
powerB_entry.place(relwidth=0.08, relx=0.87, rely=0.3)
input_button.place(relwidth=0.3, rely=0.4, relx=0.34)
result_button.place(relwidth=0.3, rely=0.4, relx=0.65)
result_label.place(relwidth=0.4, relx=0.1, rely=0.5)





root.mainloop()