from threading import Thread
import time

class Database:
	def __init__(self):
		self.value = 100
		
	def update(self,amount):
		copy = self.value
		copy += amount
		time.sleep(2)
		self.value = copy
		print("success")
	
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

t1.start()
t2.start()

t1.join()
t2.join()

d.disp()