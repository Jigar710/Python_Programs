class Test:
	a = 10
	def disp(self):
		print(self.a)
		print(Test.a)
	def update(self):
		#self.a = 100
		Test.a = 100
		
t1 = Test()
t2 = Test()

t1.disp()
t2.disp()

t1.update()
print()
t1.disp()
t2.disp()
