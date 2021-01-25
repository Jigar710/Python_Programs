import socket
import pickle

host = socket.gethostname()
port = 1600

s = socket.socket()

s.bind((host,port))

s.listen(1)

add,con = s.accept()

menu = """1. download
2. upload
0. Exit"""

files = ['client1.py','client2.py','client3.py']

add.send(menu.encode())

op = add.recv(1024).decode()

while(op!='0'):
	if(op=='1'):
		lst = pickle.dumps(files)
		add.send(lst)
		
		num = int(add.recv(1024).decode())
		file = open(files[num-1])
		data = file.read()
		add.send(data.encode())
		file.close()
		
	elif(op=='2'):
		data = add.recv(5*1024).decode()
		file = open("data.txt","w")
		file.write(data)
		file.close()
		
	op = add.recv(1024).decode()