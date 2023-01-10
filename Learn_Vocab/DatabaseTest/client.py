import socket


HEADER=64 
PORT=5050
SERVER="192.168.0.112"
DISCONNECT_MESSAGE="!DISCONNECT"
FORMAT='utf-8'
ADDR=(SERVER, PORT)


client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    send_length+=b' ' *(HEADER -len(send_length))
    client.send(send_length)
    client.send(message)
    
    print(client.recv(2048).decode(FORMAT))

send("XIN CHÀO")
input()
send("xin chào bạn")
input()
send("cảm ơn bạn")
send(DISCONNECT_MESSAGE)