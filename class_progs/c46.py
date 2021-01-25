class Test:
	def __init__(self,a):
		print("init")
	
	def __new__(cls,*args):
		print("new")
		print(args)
	
	
t = Test(10)
print(t)