import socket

ip = socket.gethostname()
port = 1600

s = socket.socket()

s.bind((ip,port))
s.listen(1)

con,add = s.accept()

while True:
	msg = input("Enter msg : " )
	con.send(msg.encode())
	
	if msg=='bye':
		break;
	
	msg = con.recv(1024).decode()
	print("client says :",msg)
		
	if msg=='bye':
		break;