import socket

host = socket.gethostname()
port = 1600

s = socket.socket()

s.connect((host,port))
print("connection done!!!")