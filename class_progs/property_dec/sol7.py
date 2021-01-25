#access normal method using class method

class Test:
	
	def disp1(self):
		print("disp1")
		
	@classmethod
	def disp2(cls):
		print("disp2")
		#cls.disp1() not allowed
		t = Test()
		t.disp1()

Test.disp2()