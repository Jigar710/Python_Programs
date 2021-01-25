class Test:
	
	def disp1(cls):
		print("disp1")
		
	@classmethod
	def disp2(cls):
		print("disp2")
		
t = Test()
t.disp1()
t.disp2()
#Test.disp2()