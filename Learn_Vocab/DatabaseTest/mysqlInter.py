import csv
from tkinter import *
import mysql.connector
from scrollbar import scroll
from tkinter import ttk

class windowSetting:
    def __init__(self,title):
        self.screen=Tk()
        self.screen.title(title)


def addFunc():
    wordTemp=wordEntry.get()
    kindTemp=kindEntry.get()
    meanTemp=meanEntry.get()
    clearInput()
    annFunc(wordTemp)
    levelTemp=levelEntry.get().upper()
    sqlCommand="INSERT INTO vocabulary (word,kind,mean,level) VALUES (%s,%s,%s,%s)"
    values=(wordTemp,kindTemp,meanTemp,levelTemp)
    if wordTemp!="" and meanTemp!="":
        cursor.execute(sqlCommand,values)
    database.commit()

def showFunc():
    supp=windowSetting("Word List")
    scrollShowall=scroll(supp.screen)

    sqlCommand="SELECT * FROM vocabulary"
    values=""
    cursor.execute(sqlCommand,values)
    result=cursor.fetchall()

    
    for index,inf in enumerate(result):
        showWord(scrollShowall.ndFrame,inf,index)

    
    selectId(supp,scrollShowall.ndFrame,index)
    """excelButton=Button(scroll.ndFrame,text="Save to Excel",width=57,command=lambda: toExcel(result))
    excelButton.grid(row=index+3,column=0, columnspan=4)
    """
    database.commit()

def showWord(screen,wordGroup,pos):
    index= Label(screen,text=str(wordGroup[4]), width=5, anchor=W, bg="#FEF7DC")
    word=Label(screen,text=wordGroup[0], width=15, anchor=W, bg="#FFEBC9")
    kind=Label(screen,text=wordGroup[1], width=5, anchor=W, bg="#FEF7DC")
    mean=Label(screen,text=wordGroup[2], width=30, anchor=W, bg="#FFEBC9")

    index.grid(column=0, row=pos)
    word.grid(column=1, row=pos)
    kind.grid(column=2, row=pos)
    mean.grid(column=3, row=pos)

def clearInput():
    wordEntry.delete(0,END)
    kindEntry.delete(0,END)
    meanEntry.delete(0,END)
    levelEntry.delete(0,END)

def toExcel(result):
    with open("vocabulary.csv","a",encoding="unicode") as f:
        w=csv.writer(f,dialect='excel')
        for inf in result:
            w.writerow(inf[2])

def searchFunc():
    def searchCommand():
        cmd=''
        cmd+='word=%s '
        if kindTemp!='' and wordTemp!='': cmd+='AND '
        else: cmd+='OR '
        cmd+='kind=%s '
        if kindTemp!='' and meanTemp!='': cmd+='AND '
        else: cmd+='OR '
        cmd+='mean=%s '
        if levelTemp!='' and meanTemp!='': cmd+='AND '
        else: cmd+='OR '
        cmd+='level=%s'
        return cmd
    supp=windowSetting("Word List")
    scrollSearch=scroll(supp.screen)
    wordTemp=wordEntry.get()
    kindTemp=kindEntry.get()
    meanTemp=meanEntry.get()
    levelTemp=levelEntry.get()
    temp=str(searchCommand())
    print(temp)
    sqlCommand=f"SELECT * FROM vocabulary WHERE {temp}"
    if levelTemp=="": levelTemp='D1'
    values=(wordTemp,kindTemp,meanTemp,levelTemp)
    cursor.execute(sqlCommand,values)

    wordList=cursor.fetchall()
    for index,word in enumerate(wordList):
        showWord(scrollSearch.ndFrame,word,index)

    selectId(supp,scrollSearch.ndFrame,index)
    database.commit()

def annFunc(wordAdd):
    annFrame=Frame(main.screen)
    annFrame.grid(row=0, column=1)
    intro=Label(annFrame,text="Annoucement",font=("Time",14))
    intro.grid(row=0, column=0, pady=(10,0))
    print(wordAdd+" alo")
    sqlCommand="SELECT * FROM vocabulary WHERE word=%s"
    value=(wordAdd, )
    cursor.execute(sqlCommand,value)
    wordList=cursor.fetchall()
    if wordList:
        ann=Label(annFrame,text="Available, use search to find")
    else:
        ann=Label(annFrame,text="Added "+wordAdd, width=20)
    ann.grid(row=1, column=0)

    database.commit()

def cleanDatabase():
    sqlCommand="DELETE FROM vocabulary WHERE mean=''"
    cursor.execute(sqlCommand)

def selectId(main,screen,index):
    def select():
        dropValue=dropBox.get()
        if dropValue=="DELETE ID":
            sqlCommand="DELETE FROM vocabulary WHERE user_id=%s"
            value=(idEntry.get(), )
            cursor.execute(sqlCommand,value)
            main.screen.destroy()
            searchFunc()
        else:
            sqlCommand="SELECT * FROM vocabulary WHERE user_id=%s"
            value=(idEntry.get(), )
            cursor.execute(sqlCommand,value)
            for inf in cursor.fetchall():
                wordEntry.insert(0,inf[0])
                kindEntry.insert(0,inf[1])
                meanEntry.insert(0,inf[2])
                levelEntry.insert(0,inf[3])
        database.commit()
    def update():
        print("update")
        sqlCommand="""UPDATE vocabulary SET word=%s, kind=%s, mean=%s, level=%s WHERE user_id=%s"""
        values=(wordEntry.get(),kindEntry.get(),meanEntry.get(), levelEntry.get() ,idEntry.get())
        cursor.execute(sqlCommand,values)
        database.commit()
        main.screen.destroy()
        searchFunc()


    dropBox=ttk.Combobox(screen, value=["EDIT ID 🤣","DELETE ID"],width=10)
    dropBox.current(0)
    idEntry=Entry(screen,width=5)
    selectButton=Button(screen,text="Select",width=10,command=lambda:select())

    
    wordEntry= Entry(screen, width=30)
    kindEntry= Entry(screen, width=30)
    meanEntry= Entry(screen, width=30)
    levelEntry=Entry(screen, width=30)
    wordLable=Label(screen,text="Word",width=10)
    kindLable=Label(screen,text="Kind",width=10)
    meanLable=Label(screen,text="Mean",width=10)
    levelLable=Label(screen,text="Level",width=10)
    wordEntry.grid(column=2, row=index+4, pady=2, columnspan=3)
    wordLable.grid(column=1, row=index+4, pady=2)
    kindEntry.grid(column=2, row=index+5, pady=2, columnspan=3)
    kindLable.grid(column=1, row=index+5, pady=2)
    meanEntry.grid(column=2, row=index+6, pady=2, columnspan=3)
    meanLable.grid(column=1, row=index+6, pady=2)
    levelEntry.grid(column=2, row=index+7, pady=2, columnspan=3)
    levelLable.grid(column=1, row=index+7, pady=2)
    addButton=Button(screen,text="SAVE",width=10, command=lambda: update())
    addButton.grid(column=1, row=index+8)   

    dropBox.grid(row=index+3, column=1, pady=(10,5))
    idEntry.grid(row=index+3, column=2, pady=5)
    selectButton.grid(row=index+3, column=3, pady=(10,5))

"""def clearDatabase():
    cursor.excute("DELETE FROM vocabulary WHERE ")"""

main=windowSetting('Leo Notebook')
database=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Leo17_08",
    database="database2"
)
cursor=database.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS vocabulary (\
    word VARCHAR(255),\
    kind VARCHAR(255),\
    mean VARCHAR(255),\
    level VARCHAR(255),\
    user_id INT AUTO_INCREMENT PRIMARY KEY\
)")



mainFrame=Frame(main.screen)
mainFrame.grid(row=0, column=0)
titleLable=Label(mainFrame, text="Vocabulary Note",font=("Helvetica",16))
titleLable.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

wordEntry= Entry(mainFrame, width=30)
kindEntry= Entry(mainFrame, width=30)
meanEntry= Entry(mainFrame, width=30)
levelEntry=Entry(mainFrame, width=30)
wordLable=Label(mainFrame,text="Word",width=10)
kindLable=Label(mainFrame,text="Kind",width=10)
meanLable=Label(mainFrame,text="Mean",width=10)
levelLable=Label(mainFrame,text="Level",width=10)


addButton=Button(mainFrame,text="Add",width=10, command=addFunc)
searchButton=Button(mainFrame,text="Seach", width=25, command=searchFunc)
showButton=Button(mainFrame,text="Show all", width=37, command=showFunc)


wordEntry.grid(column=1, row=1, pady=2)
wordLable.grid(column=0, row=1, pady=2)
kindEntry.grid(column=1, row=2, pady=2)
kindLable.grid(column=0, row=2, pady=2)
meanEntry.grid(column=1, row=3, pady=2)
meanLable.grid(column=0, row=3, pady=2)
levelEntry.grid(column=1, row=4, pady=2)
levelLable.grid(column=0, row=4, pady=2)

addButton.grid(column=0, row=5)
searchButton.grid(column=1, row=5)
showButton.grid(column=0, row=6, columnspan=2)

cleanDatabase()


main.screen.mainloop()