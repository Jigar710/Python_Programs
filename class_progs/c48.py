class Demo:
	def __init__(self):
		print("this is demo")
		return None
		
class Test:
	def __init__(self):
		print("init")
	def __new__(cls):
		print("oye wait will do some magic")
		#return super().__new__(Demo)
		return super().__new__(Demo)
		
t = Test()
print(t)

print(Demo.__new__(Demo))
