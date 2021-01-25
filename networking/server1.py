import socket

host = socket.gethostname()
port = 1600

s = socket.socket()

s.bind((host,port))

s.listen(1)
'''
add = s.accept()
print(type(add))
print(add)
'''
add,con = s.accept()
print("address info : ",add)
print("connection : ",con)