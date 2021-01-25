class Demo:
	def __init__(self):
		print("this is demo")
	
	def __new__(cls):
		return super().__new__(cls)
		
class Test:
	def __new__(cls):
		print("oye wait will do some magic")
		#return super().__new__(Demo)
		return Demo.__new__(Demo)
		
t = Test()
print(t)
