import socket
import pickle
import Employee

ip = socket.gethostname()
port = 1600

s = socket.socket()

s.bind((ip,port))
s.listen(1)

con,add = s.accept()

e = Employee.Emp()
e.set("aaa",10,10000)

e = pickle.dumps(e)
con.send(e)