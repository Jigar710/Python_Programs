#nested function

def m2():
	print("this is m2")
	m1()

def m1():
	print("this is m1")

	
m2()