import sqlite3

def processWord(temp):
    return(temp[0:len(temp)-1].split(":"))


database=sqlite3.connect('database1.db')
cursor=database.cursor()

f1=open("Vocab.txt","rb")
while True :
    temp=f1.readline()
    if not temp: break
    temp=processWord(temp.decode("utf-8"))
    kind=temp[1][temp[1].index("(")+1:temp[1].index(")")]
    mean=temp[1][0:temp[1].index("(")-1]
    cursor.execute("INSERT INTO vocabulary VALUES (:word, :kind, :mean)",
            {
                'word': temp[0],
                'kind': kind,
                'mean': mean
            }
        )
    print(mean+" "+kind)
f1.close()





database.commit()
database.close()