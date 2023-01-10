from email import message
import glob
from tkinter import *
from random import *
from tkinter import messagebox
from tracemalloc import stop
from cv2 import correctMatches, mean
import mysql.connector
COLOR_1 = '#FFEDD3'
COLOR_2 = '#FCD2D1'
COLOR_3 = '#FE8F8F'
COLOR_4 = '#FF5C58'

main = Tk()
main.title("Leo Notebook")
main.geometry("500x300")
main.resizable(0,0)

def learnFunc(*arg):
    numEntry.config(state="disabled")
    numButton.config(state="disabled")
    ansEntry.config(state="normal")
    ansButton.config(state="normal")
    pssButton.config(state="normal")
    try:
        stopPoint = int(numEntry.get())
    except ValueError:
        stopPoint = len(wordList)
    listLen = len(wordList)
    global count
    global correct
    global passed
    temp = 0
    if count <= stopPoint:
        while not (temp in wordLearned): 
            temp = randint(0,listLen)
            if not (temp in wordLearned): break
        global wordLearning
        wordLearning = wordList[temp][0]
        count+=1
        wordLearned.append(temp)
        meanEntry.delete(0,END)
        kindEntry.delete(0,END)
        meanEntry.insert(0,wordList[temp][2])
        kindEntry.insert(0,wordList[temp][1]) 
    else: 
        messagebox.showinfo("Information","Finish Learning")
        numEntry.config(state="normal")
        numButton.config(state="normal")
        ansEntry.config(state="disabled")
        ansButton.config(state="disabled")
        pssButton.config(state="disabled")
        print(correct)
        print(passed)
        
        correct=[]
        passed=[]
        count=0
        clearFunc()
        reFunc()
    return 0

def checkFunc(*arg):
    global correct
    if ansEntry.get() == wordLearning:
        correct.append(wordLearning)
        clearFunc()
        learnFunc()
    else: messagebox.showinfo("Information","Wrong, Try again")
    return 0

def passFunc(*arg):
    global passed
    passed.append(wordLearning)
    clearFunc()
    learnFunc()
    return 0
def clearFunc():
    meanEntry.delete(0,END)
    kindEntry.delete(0,END)
    ansEntry.delete(0,END)
    return 0

def reFunc():
    reFrame.place(relwidth=0.9, relheight=0.7, relx=0.05, rely=0.2)
    return 0

def continueFunc():
    toFrame.place(relwidth=0, relheight=0)
    return 0
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Leo17_08",
    database="database2"
)
cursor=database.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS vocabulary(\
    word VARCHAR(255),\
    kind VARCHAR(255),\
    mean VARCHAR(255),\
    level VARCHAR(255),\
    user_id INT AUTO_INCREMENT PRIMARY KEY\
)")
sqlCommand="SELECT * FROM vocabulary"
values=""
cursor.execute(sqlCommand,values)
wordList=cursor.fetchall()
global wordLearned
global count
global correct
global passed

wordLearned = []
correct=[]
passed=[]
count = 0

frame = Frame(main)
canvas = Canvas(frame)

inFrame = Frame(frame)
ouFrame = Frame(frame)
toFrame = Frame(frame)
reFrame = Frame(frame)
inCanvas = Canvas(inFrame)
ouCanvas = Canvas(ouFrame)
reCanvas = Canvas(reFrame)
nameLabel = Label(main, text="LEARN VOCABULARY")

guildLabel = Label(toFrame, text="How To Use")
detailLabel = Text(toFrame)
numLabel = Label(inFrame, text="No. words")
numEntry = Entry(inFrame)
numButton = Button(inFrame, text="LEARN")

meanLabel = Label(ouFrame, text="Meaning")
kindLabel = Label(ouFrame, text="Kind")
meanEntry = Entry(ouFrame)
kindEntry = Entry(ouFrame)
ansLabel = Label(ouFrame, text="Answer")
ansEntry = Entry(ouFrame)
ansButton = Button(ouFrame, text="CHECK")
pssButton = Button(ouFrame, text="PASS")

r = IntVar()
continueButton = Button(toFrame, text="CONTINUE")

ansEntry.bind('<Return>',checkFunc)
numEntry.bind('<Return>',learnFunc)
pssButton.bind('<Return>',passFunc)
ansButton.bind('<Return>',checkFunc)

frame.config(bg=COLOR_1)
canvas.config(bg=COLOR_1)
inFrame.config(bg=COLOR_3)
ouFrame.config(bg=COLOR_3)
toFrame.config(bg=COLOR_3)
reFrame.config(bg=COLOR_3)
inCanvas.config(bg=COLOR_3)
ouCanvas.config(bg=COLOR_3)
reCanvas.config(bg=COLOR_3)

nameLabel.config(bg=COLOR_2, font="Time 12 bold italic")
numLabel.config(bg=COLOR_1)
numButton.config(relief="flat",bg=COLOR_1,command=lambda:learnFunc())

detailLabel.insert(END,"  Enter number of word \n   you want to review\n","center")
detailLabel.insert(END,"\n  EG: 1,2,3,4,...,all")

guildLabel.config(bg=COLOR_1, relief="flat")
detailLabel.config(bg=COLOR_1, relief="flat")
meanLabel.config(bg=COLOR_1)
kindLabel.config(bg=COLOR_1)
meanEntry.config(bg=COLOR_1,relief="flat")
kindEntry.config(bg=COLOR_1,relief="flat")
ansLabel.config(bg=COLOR_1)
ansEntry.config(state="disabled")
ansButton.config(relief="flat",bg=COLOR_1,command=lambda:checkFunc(), state='disabled')
pssButton.config(relief="flat",bg=COLOR_1, command=lambda:passFunc(), state='disabled')
continueButton.config(relief="flat", bg=COLOR_1, command=lambda:continueFunc())

inCanvas.create_line(0,95,300,95,fill=COLOR_1)
ouCanvas.create_line(0,95,300,95,fill=COLOR_1)

frame.place(relheight=1, relwidth=1)
#canvas.place(relheight=0.5, relwidth=0.5, relx=0.25, rely=0.25)
inFrame.place(relwidth=0.425, relheight=0.7, relx=0.05, rely=0.2)
ouFrame.place(relwidth=0.425, relheight=0.7, relx=0.525, rely=0.2)
toFrame.place(relwidth=0.425, relheight=0.7, relx=0.05, rely=0.2)
inCanvas.place(relwidth=1, relheight=1)
ouCanvas.place(relwidth=1, relheight=1)

guildLabel.place(relwidth=0.9, relheight=0.1, rely=0.1, relx= 0.05)
detailLabel.place(relwidth=0.9, relheight=0.4, rely=0.275, relx=0.05)
continueButton.place(relwidth=0.4, relheight=0.1, rely=0.75, relx=0.55)

nameLabel.place(relwidth=0.9, relheight=0.1, rely= 0.05, relx= 0.05)
numLabel.place(relwidth=0.4, relheight=0.1, relx=0.05, rely=0.1)
numEntry.place(relwidth=0.45, relheight=0.1, relx=0.5, rely=0.1)
numButton.place(relwidth=0.45,relheight=0.1,relx=0.5, rely=0.25)

meanLabel.place(relwidth=0.3, relheight=0.1, relx=0.05, rely=0.1)
kindLabel.place(relwidth=0.3, relheight=0.1, relx=0.05, rely=0.25)
meanEntry.place(relwidth=0.55, relheight=0.1, relx=0.4, rely=0.1)
kindEntry.place(relwidth=0.55, relheight=0.1, relx=0.4, rely=0.25)
ansLabel.place(relwidth=0.3, relheight=0.1, relx=0.05, rely=0.6)
ansEntry.place(relwidth=0.55, relheight=0.1, relx=0.4, rely=0.6)
ansButton.place(relwidth=0.25,relheight=0.1,relx=0.7, rely=0.75)
pssButton.place(relwidth=0.25,relheight=0.1,relx=0.4, rely=0.75)
main.mainloop()
