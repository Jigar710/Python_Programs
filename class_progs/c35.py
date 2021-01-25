class Test:
	a = 10
	def disp1(self):
		self.b = 20
		print(self.b)
		print("called by object")
		
	@classmethod
	def disp2(cls):
		print("called by class")
		cls.a = 100
		cls.b = 99

	def bi(self):
		print(self.b)
t1 = Test()
t2 = Test()

t2.disp1()
t2.disp2()
print(Test.a)
print(t2.b)