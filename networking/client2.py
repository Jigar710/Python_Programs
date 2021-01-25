import socket

ip = socket.gethostname()
port = 1600

s = socket.socket()

s.connect((ip,port))

data = s.recv(1024)
print(data.decode())