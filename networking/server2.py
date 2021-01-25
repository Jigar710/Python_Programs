import socket

ip = socket.gethostname()
port = 1600

s = socket.socket()

s.bind((ip,port))

s.listen(1)

add,con = s.accept()

add.send("hiiiii...".encode())