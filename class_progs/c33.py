class Test:
	a = 10
	def disp(self):
		print(self.a)
		print(Test.a)
	
t1 = Test()
t2 = Test()

t1.disp()
t2.disp()