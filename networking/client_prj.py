import socket
import pickle
from Employee import Emp

host = socket.gethostname()
port = 1600

s = socket.socket()
s.connect((host,port))

menu = s.recv(1024).decode()
print(menu)

op = input("Enter option : ")
s.send(op.encode())

while(op!='0'):
	if(op=='1'):
		e = Emp()
		e.set(input("Name : "),input ("Age : "),input("Sal : "))
		e = pickle.dumps(e)
		s.send(e)
		print(s.recv(1024).decode())
	
	elif(op=='4'):
		emps = s.recv(2048)
		emps = pickle.loads(emps)
		
		for e in emps:
			e.disp()
		
	elif(op=='5'):
		name = input("Enter name of emp : ")
		s.send(name.encode())
		
		rst = s.recv(1024).decode()
		
		if(rst=='success'):
			e = s.recv(1024)
			e = pickle.loads(e)
			e.disp()
		else:
			print("no record found")
	
	op = input("Enter option : ")
	s.send(op.encode())