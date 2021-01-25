#nested function
def m1():
	print("this is m1")

def m2():
	print("this is m2")
	m1()
	
m2()