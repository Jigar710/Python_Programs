import socket
import threading

ip = socket.gethostname()
port = 1600

s = socket.socket()
s.connect((ip,port))
flag = True
def send_method():
	global flag
	while(flag):
		try:
			msg = input("Client@ :")
			s.send(msg.encode())
		except:
			flag = False
			msg = "kill"
			s.send(msg.encode())
			break;

def rec_method():
	global flag
	while(flag):
		msg = s.recv(1024).decode()
		print("Server :",msg)
		if msg == "kill":
			flag = False
			break;
	
		

t1 = threading.Thread(target=send_method)
t2 = threading.Thread(target=rec_method)

t1.start()
t2.start()