#create thread from daemon thread
import threading
import time

def firstmethod():
	t2 = threading.Thread(target=secmethod)	
	print("t2 : ",t2.isDaemon())
	t2.start()
	for i in range(1,3):
		print(threading.current_thread().name,i)
		time.sleep(1)
		
def secmethod():
	for i in range(10,51,10):
		print(threading.current_thread().name,i)
		time.sleep(1)

t1 = threading.Thread(target=firstmethod,daemon=True)
print("t1 : ",t1.isDaemon())
t1.start()
print("t1 : ",t1.isDaemon())
print("main : ",threading.current_thread().isDaemon())