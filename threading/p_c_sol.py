#ITC : inter thread communication
from threading import Thread,Condition
import time

class res:
	def __init__(self):
		self.value = 0
		self.cv = Condition()
		self.flag = True
		
	def set(self,value):
		self.cv.acquire()
		while(self.flag == False):
			self.cv.wait()
		self.value = value
		print("set : ",self.value)
		self.flag = False
		self.cv.notify()
		self.cv.release()
		
	def get(self):
		self.cv.acquire()
		while(self.flag==True):
			self.cv.wait()
		print("get : ",self.value)
		self.flag = True
		self.cv.notify()
		self.cv.release()

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

t2.start()		
t1.start()		