class time:
	def set(t,a,b,c):
		t.h = a
		t.m = b
		t.s = c

	def disp(self):
		print(self.h,self.m,self.s)
		
		
t1 = time()
t2 = time()

t1.set(1,2,3)
t2.set(10,20,30)

t1.disp()
t2.disp()