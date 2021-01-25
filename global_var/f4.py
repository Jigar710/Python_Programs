def m1():
	print('welcome from m1')
	def m2():
		print("welcoem from m2")
		print("bye from m2")
		return "this is m2"
	print("bye from m1")
	return m2()
	
a = m1()
print(a)