class Test:
	def __init__(cls):
		print("init")
		#return "hello"
		return None
		
t = Test()
print("value : ",t)
print(type(t))