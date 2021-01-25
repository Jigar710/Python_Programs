import threading 

def method1():
	print("hello")
	
def method2():
	print("hi")
	
	
t1 = threading.Thread(target=method1)
t2 = threading.Thread(target=method2)

t1.start()
t2.start()