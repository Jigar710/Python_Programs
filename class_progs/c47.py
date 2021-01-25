class Test:
	def __init__(self):
		print("init")
	
	def __new__(cls,*args):
		print("new")
		#print(args)
		return super().__new__(cls)
	
t = Test()
print(t)