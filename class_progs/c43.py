class Test:
	def __new__(cls):
		print("new")
		
		
t = Test()
print("value : ",t)
print(type(t))