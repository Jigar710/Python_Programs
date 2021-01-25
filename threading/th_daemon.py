#Daemon thread : service thread

import threading
import time

def firstmethod():
	for i in range(1,3):
		print(threading.current_thread().name,i)
		time.sleep(1)
		
def secmethod():
	for i in range(10,51,10):
		print(threading.current_thread().name,i)
		time.sleep(1)
		
t1 = threading.Thread(target = firstmethod,name='First thread')
t2 = threading.Thread(target = secmethod,name = 'Second thread')
print("welcome to main")

print(t1.isDaemon())
print(t2.isDaemon())
t1.start()
t2.start()
print("bye from main")