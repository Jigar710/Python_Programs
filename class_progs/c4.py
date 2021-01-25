class time:
	def set(t,a,b,c):
		t.h = a
		t.m = b
		t.s = c

	def disp(self):
		print(self.h,self.m,self.s)

t1 = time()
t2 = time()
t3 = time()

t1.set(1,2,3)
t2.set(10,20,30)

t3.h = t1.h + t2.h
t3.m = t1.m + t2.m
t3.s = t1.s + t2.s

t3.disp()
