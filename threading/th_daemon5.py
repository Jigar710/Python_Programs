#create thread from non-daemon thread
import threading

def FirstMethod():
	t2 = threading.Thread()	
	print("t2 : ",t2.isDaemon())
	
t1 = threading.Thread(target=FirstMethod)
print("t1 : ",t1.isDaemon())
t1.start()
print("main : ",threading.current_thread().isDaemon())