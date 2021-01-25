import socket
import pickle

host = socket.gethostname()
port = 1600

s = socket.socket()
s.connect((host,port))

menu = s.recv(1024).decode()
print(menu)

op = input("Enter your choice : ")
s.send(op.encode())

while(op!='0'):
	if(op=='1'):
		lst = s.recv(2048)
		lst = pickle.loads(lst)
		if(len(lst)==0):
			print("no files")
		else:
			for i in range(len(lst)):
				print(i+1,".",lst[i])
			num = input("Enter file number : ")
			s.send(num.encode())
			
			data = s.recv(1024*5).decode()
			
			file = open("temp.txt","w")
			file.write(data)
			file.close()
			
	elif(op=='2'):
		name = input("Enter file name : ")
		file = open(name)
		data = file.read()
		s.send(data.encode())
		file.close()
		
	op = input("Enter your choice : ")
	s.send(op.encode())
