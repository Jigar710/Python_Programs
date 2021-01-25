#pass function as an arg to other funct

def m1():
	print("this is m1 method")
	
def m2(x):
	print("welcoem to m2")
	x()
	print("bye from m2")
	
	

m2(m1)