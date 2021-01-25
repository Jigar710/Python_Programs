import socket
import pickle

ip = socket.gethostname()
port = 1600

s = socket.socket()
s.connect((ip,port))

l = s.recv(1024)
print(l)
l = pickle.loads(l)
print(l)