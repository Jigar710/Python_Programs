import socket
import pickle

host = socket.gethostname()
port = 1600

s = socket.socket()

s.bind((host,port))

s.listen(1)

add,con = s.accept()

emps = []
menu = """1. insert 
2. delete
3. udpate
4. disp
5. search
0. Exit"""

add.send(menu.encode())

op = add.recv(1024).decode()
while(op!='0'):
	if(op=='1'):
		e = add.recv(2048)
		e = pickle.loads(e)
		emps.append(e)
		add.send("inserted...".encode())
		#print(len(emps))
		
	elif(op=='4'):
		temp_emps = pickle.dumps(emps)
		add.send(temp_emps)
		
	elif(op=='5'):
		name = add.recv(1024).decode()
		
		rst = "fail"
		for e in emps:
			if(e.getName() == name):	
				rst = "success"
				add.send(rst.encode())
				temp = pickle.dumps(e)
				add.send(temp)
				break
		if(rst == 'fail'):
			add.send(rst.encode())
			
	op = add.recv(1024).decode()