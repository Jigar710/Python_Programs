import socket
import pickle

ip = socket.gethostname()
port = 1600

s = socket.socket()

s.bind((ip,port))
s.listen(1)

con,add = s.accept()

#l = [1,2,3,4,5]
#l = (1,2,3,4,5)
l = {'a':100,'b':200}
l = pickle.dumps(l)
con.send(l)