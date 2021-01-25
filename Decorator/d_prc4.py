def m1(func):
	print("welcome from outer")
	func()
	print("bye from outer")
def m2():
	print("inner")
	
m1(m2)