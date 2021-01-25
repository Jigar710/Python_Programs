class Test:
	def disp1(self):
		print("disp1")
		self.disp2()
		
	def disp2(self):
		print("disp2")
		
		
t1 = Test()
t1.disp1()
