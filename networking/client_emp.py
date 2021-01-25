import socket
import pickle
import Employee

ip = socket.gethostname()
port = 1600

s = socket.socket()
s.connect((ip,port))

e = s.recv(1024)

e = pickle.loads(e)
e.disp()