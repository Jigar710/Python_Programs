#access class method using normal method

class Test:
	
	def disp1(self):
		print("disp1")
#		Test.disp2()
		self.disp2()
		
	@classmethod
	def disp2(cls):
		print("disp2")
		
t = Test()
t.disp1()
