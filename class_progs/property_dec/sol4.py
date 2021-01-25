class Test:
	@classmethod
	def disp1(cls):
		print("disp1")
		#cls.disp2()
		Test.disp2()
		
	@classmethod
	def disp2(cls):
		print("disp2")
		
		
Test.disp1()

t = Test()
t.disp1()
