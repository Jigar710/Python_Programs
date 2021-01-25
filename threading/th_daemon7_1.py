#create thread from daemon thread
import threading

def FirstMethod():
	t2 = threading.Thread(daemon=False)	
	print("t2 : ",t2.isDaemon())
	
t1 = threading.Thread(target=FirstMethod,daemon=True)
print("t1 : ",t1.isDaemon())
t1.start()
print("t1 : ",t1.isDaemon())
print("main : ",threading.current_thread().isDaemon())