class time:
	def set(self,h,m,s):
		self.h = h
		self.m = m
		self.s = s
		
	def disp(self):
		print(self.h,self.m,self.s)

	def add(self,x,y):
		self.h = x.h + y.h
		self.m = x.m + y.m
		self.s = x.s + y.s
		
t1 = time()
t2 = time()
t3 = time()

t1.set(1,2,3)
t2.set(10,20,30)

#t3 = t1 + t2
t3.add(t1,t2)

t3.disp()