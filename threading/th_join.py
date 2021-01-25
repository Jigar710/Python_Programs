import threading
import time

def firstmethod():
	for i in range(1,6):
		print(threading.current_thread().name,i)
		time.sleep(1)
		
def secmethod():
	for i in range(10,51,10):
		print(threading.current_thread().name,i)
		time.sleep(1)
		
t1 = threading.Thread(target = firstmethod,name='First thread')
t2 = threading.Thread(target = secmethod,name = 'Second thread')
print("welcome to main")
t1.start()
t2.start()
t1.join()
t2.join()
print("bye from main")