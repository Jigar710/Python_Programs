#magic method
class Time:
	def __init__(self,h=0,m=0,s=0):
		self.h = h
		self.m = m
		self.s = s
		
	def disp(self):
		print(self.h,self.m,self.s)

	def __add__(self,t):
		print("+")
		t2 = Time()
		t2.h = self.h + t.h
		t2.m = self.m + t.m
		t2.s = self.s + t.s
		
		return t2
		
	def __sub__(self,t):
		print("-")
		t2 = Time()
		t2.h = self.h - t.h
		t2.m = self.m - t.m
		t2.s = self.s - t.s
		
		return t2
		
	def __truediv__(self,t):
		print("/")
		t2 = Time()
		t2.h = self.h / t.h
		t2.m = self.m / t.m
		t2.s = self.s / t.s
		
		return t2
		
	def __mul__(self,t):
		print("*")
		t2 = Time()
		t2.h = self.h * t.h
		t2.m = self.m * t.m
		t2.s = self.s * t.s
		
		return t2
		
		
t1 = Time(10,20,30)
t2 = Time(2,4,5)
t3 = Time(1,10,2)
t4 = Time(1,8,3)
t5 = Time(10,1,2)

t6 = t1 + t2 - t3 * t4 / t5
'''
t6 = t1.__add__(t2).__sub__(t3).__mul__(t4).__div__(t5)
t6 = x1.__sub__((t3.__mul__(t4)).__div__(t5)
t6 = x1.__sub__(x2.__div__(t5))
t6 = x1.__sub__(x3)
'''
t6.disp()