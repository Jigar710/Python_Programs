from threading import Thread,Lock
import time

class Database:
	def __init__(self):
		self.value = 100
		self.lock = Lock()
		
	def update(self,amount):
		self.lock.acquire()
		copy = self.value
		copy += amount
		time.sleep(2)
		self.value = copy
		print("success")
		self.lock.release()
	
	def disp(self):
		print(self.value)
		

class Mythread(Thread):
	def __init__(self,d,amount):
		self.d = d
		self.amount = amount
		super().__init__()
	def run(self):
		self.d.disp()
		self.d.update(self.amount)
		self.d.disp()
	
d = Database()	
t1 = Mythread(d,10)
t2 = Mythread(d,5)
t3 = Mythread(d,50)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

d.disp()