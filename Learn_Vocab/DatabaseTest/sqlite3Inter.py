from scrollbar import scroll
from tkinter import *
import sqlite3


class windowSetting:
    def __init__(self,title):
        self.screen=Tk()
        self.screen.title(title)

def databaseSetting(func):
    def alter():
        global database
        global cursor
        database=sqlite3.connect('database1.db')
        cursor = database.cursor()
        func()
        database.commit()
        database.close()
    return alter

@databaseSetting
def addFunc():
    wordTemp=wordEntry.get()
    kindTemp=kindEntry.get()
    meanTemp=meanEntry.get()
    if wordTemp!="" and meanTemp!="":
        cursor = database.cursor()
        cursor.execute("INSERT INTO vocabulary VALUES (:word, :kind, :mean)",
            {
                'word': wordTemp,
                'kind': kindTemp,
                'mean': meanTemp
            }
        )
    checkWordStatus(wordTemp)
    wordEntry.delete(0,END)
    meanEntry.delete(0,END)
    kindEntry.delete(0,END)

@databaseSetting
def showFunc():
    support=windowSetting('Word List')
    scroll.Setting(support.screen)
    cursor.execute("SELECT *, oid FROM vocabulary")
    wordList = cursor.fetchall()
    for word in wordList:
        if word[0] and word[2]:
            showWord(scroll.ndFrame,word,wordList.index(word))

@databaseSetting
def databaseClean():
    cursor.execute("DELETE from vocabulary WHERE word=''")
    cursor.execute("SELECT *, oid from vocabulary")
    wordList=cursor.fetchall()
    print(wordList)

def checkWordStatus(wordTemp):
    support=windowSetting('Word List')
    scroll.Setting(support.screen)
    cursor.execute("SELECT *, oid FROM vocabulary WHERE word = '%s'" % wordTemp)
    wordList = cursor.fetchall()
    for word in wordList:
        if word[0] and word[2]:
            showWord(scroll.ndFrame,word,wordList.index(word))

def showWord(screen,wordGroup,pos):
    word=Label(screen,text=wordGroup[0], width=15, anchor=W, bg="#FFEBC9")
    kind=Label(screen,text=wordGroup[1], width=5, anchor=W, bg="#FEF7DC")
    mean=Label(screen,text=wordGroup[2], width=30, anchor=W, bg="#FFEBC9")

    word.grid(column=0, row=pos)
    kind.grid(column=1, row=pos)
    mean.grid(column=2, row=pos)

main=windowSetting('Database 1.0')
database=sqlite3.connect('database1.db')

cursor = database.cursor()

wordEntry= Entry(main.screen, width=30)
kindEntry= Entry(main.screen, width=30)
meanEntry= Entry(main.screen, width=30)
wordLable=Label(main.screen,text="Word",width=10)
kindLable=Label(main.screen,text="Kind",width=10)
meanLable=Label(main.screen,text="Mean",width=10)

addButton=Button(main.screen,text="Add",width=36, command=addFunc)
showButton=Button(main.screen,text="Show", width=36, command=showFunc)

wordEntry.grid(column=1, row=0, pady=2)
wordLable.grid(column=0, row=0, pady=2)
kindEntry.grid(column=1, row=1, pady=2)
kindLable.grid(column=0, row=1, pady=2)
meanEntry.grid(column=1, row=2, pady=2)
meanLable.grid(column=0, row=2, pady=2)

addButton.grid(column=0, row=3, columnspan=2)
showButton.grid(column=0, row=4, columnspan=2)



main.screen.mainloop()
