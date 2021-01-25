class Test:
	a = 89
	@classmethod
	def abcd(cls):
		print(cls.a)
		
	@staticmethod
	def disp():
		print("this is static method")
		print(Test.a)
		print(Test.abcd())


Test.disp()

t = Test()
t.disp()