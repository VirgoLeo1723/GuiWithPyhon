from tkinter import *
import mysql.connector
from mysql.connector import cursor



main=Tk()
main.title('Database 2.0')
database=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Leo17_08",
    database="database2"
)
#print(database)
cursor=database.cursor()
#cursor.execute("CREATE DATABASE database2")
#cursor.execute("SHOW DATABASES")


cursor.execute("CREATE TABLE IF NOT EXISTS vocabulary (\
    word VARCHAR(255),\
    kind VARCHAR(255),\
    mean VARCHAR(255),\
    level VARCHAR(255),\
    user_id INT AUTO_INCREMENT PRIMARY KEY\
)")


"""cursor.execute("SELECT * FROM vocabulary")
for inf in cursor.description:
    print(inf)"""

titleLable=Label(main, text="Vocabulary Note",font=("Helvetica",16))
titleLable.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

wordEntry= Entry(main, width=30)
kindEntry= Entry(main, width=30)
meanEntry= Entry(main, width=30)
levelEntry=Entry(main, width=30)
wordLable=Label(main,text="Word",width=10)
kindLable=Label(main,text="Kind",width=10)
meanLable=Label(main,text="Mean",width=10)
levelLable=Label(main,text="Level",width=10)


addButton=Button(main,text="Add",width=37)
showButton=Button(main,text="Show", width=37)

wordEntry.grid(column=1, row=1, pady=2)
wordLable.grid(column=0, row=1, pady=2)
kindEntry.grid(column=1, row=2, pady=2)
kindLable.grid(column=0, row=2, pady=2)
meanEntry.grid(column=1, row=3, pady=2)
meanLable.grid(column=0, row=3, pady=2)
levelEntry.grid(column=1, row=4, pady=2)
levelLable.grid(column=0, row=4, pady=2)

addButton.grid(column=0, row=5, columnspan=2)
showButton.grid(column=0, row=6, columnspan=2)



main.mainloop()