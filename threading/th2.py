import threading
import time

def firstmethod():
	for i in range(1,6):
		print(i)
		time.sleep(1)
		
def secmethod():
	for i in range(10,51,10):
		print(i)
		time.sleep(1)
		
t1 = threading.Thread(target=firstmethod)
t2 = threading.Thread(target=secmethod)

t1.start()
t2.start()