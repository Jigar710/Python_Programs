class Test:
	def __init__(self):
		print("init")
		
	def __new__(cls):
		print("new")
		
t = Test()
print(t)