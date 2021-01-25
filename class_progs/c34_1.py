class Test:
	a = 10
	def disp(self):
		print(self.a)
		print(Test.a)
		
t1 = Test()
t2 = Test()

t1.disp()
t2.disp()

t1.a = 100

t1.disp()
t2.disp()
