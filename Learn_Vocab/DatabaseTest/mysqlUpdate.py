import mysql.connector

def processWord(temp):
    return(temp[0:len(temp)-1].split(":"))

database=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Leo17_08",
    database="database2"
)
cursor=database.cursor()


f1=open("Vocab.txt","rb")
while True :
    temp=f1.readline()
    if not temp: break
    temp=processWord(temp.decode("utf-8"))
    kind=temp[1][temp[1].index("(")+1:temp[1].index(")")]
    mean=temp[1][0:temp[1].index("(")-1]
    sqlCommand="INSERT INTO vocabulary (word,kind,mean,level) VALUES (%s,%s,%s,%s)"
    values=(temp[0],kind,mean,"")
    if temp[0]!=0:
        cursor.execute(sqlCommand,values)
f1.close()

cursor.execute("SELECT * FROM vocabulary")
for inf in cursor.fetchall():
    print(inf)


database.commit()

