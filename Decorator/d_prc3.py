def m1():
	print("welcome from outer")
	def m2():
		print("inner")
	
	print("bye from outer")
	return m2()
	
x = m1()
print(x)