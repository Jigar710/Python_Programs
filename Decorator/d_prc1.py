def m1():
	print("welcome from outer")
	def m2():
		print("inner")
	m2()
	print("bye from outer")
	
m1()