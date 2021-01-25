import socket

ip = socket.gethostname()
port = 1600

s = socket.socket()
s.connect((ip,port))


while True:
	msg = s.recv(1024).decode()
	print("server says :",msg)
		
	if msg=='bye':
		break;
		
	msg = input("Enter msg : ")
	s.send(msg.encode())
		
	if msg=='bye':
		break;