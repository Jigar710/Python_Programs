#access instance variable inside class within class method and normal method
class Test:
	a = 99
	def set(self,a):
		self.a = a
		
	def disp1(self):
		print(self.a)
		#print(Test.a) #not allowed 
		
	@classmethod
	def disp2(cls):
		print(cls.a)	
		
		
t = Test()
t.set(100)
t.disp1()
t.disp2()