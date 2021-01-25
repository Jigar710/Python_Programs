import socket
import threading
import time
ip = socket.gethostname()
port = 1600

s = socket.socket()

s.bind((ip,port))
s.listen(1)

con,add = s.accept()

flag = True

def send_method():
	global flag
	while(flag):
		try:
			msg = input("Server@ : ")
			con.send(msg.encode())
		except:
			flag = False
			msg = "kill"
			con.send(msg.encode())
			break
			
def rec_method():
	global flag
	while(flag):
		msg = con.recv(1024).decode()
		print("client :",msg)
		if msg == "kill":
			flag = False
			break;
		

	
t1 = threading.Thread(target=send_method)
t2 = threading.Thread(target=rec_method)

t1.start()
t2.start()
t1.join()
t2.join()