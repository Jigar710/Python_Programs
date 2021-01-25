from threading import Thread,Condition

class res:
	def __init__(self):
		self.n = 0
	def disp1(self,n):
		self.n = n
		print("disp1 : ",self.n)
	def disp2(self):
		self.n = self.n * 10
		print("disp2 : ",self.n)
	def disp3(self):
		self.n = self.n * 100
		print("disp3 : ",self.n)
		
class Mythread1(Thread):	
	def __init__(self,r):
		self.r = r
		super().__init__()
	def run(self):
		for i in range(1,11):
			r.disp1(i)
class Mythread2(Thread):	
	def __init__(self,r):
		self.r = r
		super().__init__()
	def run(self):
		for i in range(1,11):
			r.disp2()
class Mythread3(Thread):	
	def __init__(self,r):
		self.r = r
		super().__init__()
	def run(self):
		for i in range(1,11):
			r.disp3()
			
r = res()

t1 = Mythread1(r)
t2 = Mythread2(r)
t3 = Mythread3(r)

t1.start()
t2.start()
t3.start()