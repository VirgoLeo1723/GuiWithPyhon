from tkinter import *
import sqlite3 

root=Tk()
root.title('Database 1.0')
root.geometry('400x400')

# Create a database or connect to one
database=sqlite3.connect('database1.db')

# Create cursor
cursor = database.cursor()

# Create table
cursor.execute("""CREATE TABLE vocabulary (
    word text,
    kind text,
    mean text
)""")

# Commit changes
database.commit()

# Close connection
database.close()

root.mainloop()