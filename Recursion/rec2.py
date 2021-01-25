#indirect recursion
def disp():
	print("hello")
	show()
	
def show():
	print("hi")
	disp()
	
print("before recursion")
disp()
print("after recursion")