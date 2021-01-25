from threading import Thread
import time
class res:
	def __init__(self):
		self.value = 0
	def set(self,value):
		self.value = value
		print("set : ",self.value)

	def get(self):
		print("get : ",self.value)

class Producer(Thread):
	def __init__(self,r):
		self.r = r
		super().__init__()
	def run(self):
		for i in range(1,11):
			self.r.set(i)
		
class Consumer(Thread):
	def __init__(self,r):
		self.r = r
		super().__init__()
		
	def run(self):
		for i in range(1,11):
			self.r.get()
	
r = res()	
t1 = Producer(r)
t2 = Consumer(r)

t1.start()		
t2.start()		