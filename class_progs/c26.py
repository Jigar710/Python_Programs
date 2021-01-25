class time:
	def set(self,h,m,s):
		self.h = h
		self.m = m
		self.s = s
	
	def disp(self):
		print(self.h,self.m,self.s)

	def __add__(self,x):
		print("+")
		t = time()
		
		t.h = self.h + x.h
		t.m = self.m + x.m
		t.s = self.s + x.s
		
		return t	
	
	def __sub__(self,x):
		print("-")
		t = time()
		
		t.h = self.h - x.h
		t.m = self.m - x.m
		t.s = self.s - x.s
		
		return t
		
	def __truediv__(self,x):
		print("/")
		return x
		
	def __mul__(self,x):
		print("*")
		return x
		
	
t1 = time()
t2 = time()
t3 = time()
t4 = time()

t1.set(1,2,3)
t2.set(10,20,30)
t3.set(100,200,300)

#t4 = t1 + t2 - t3 * t1 / t2 
t4 = t1 + t2 * t3 - t1 / t2 
'''
x = t3 * t1
y = x / t2
z = t1 + t2
t4 = z - y
'''
'''
t4 = x - t3 * t1 / t2 
t4 = x - y / t2 
t4 = x - z
'''
t4.disp()
# + * / -

