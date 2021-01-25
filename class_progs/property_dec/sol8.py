#access class variable inside class within class method and normal method
class Test:
	a = 10		#class variable
	
	def disp1(self):
		print(self.a)
		print(Test.a)
		
	@classmethod
	def disp2(cls):
		print(cls.a)	#cls means Test (class itself)
		print(Test.a)
		
t = Test()
t.disp1()
Test.disp2()
t.disp2()