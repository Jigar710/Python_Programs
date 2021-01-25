#direct recursion
def disp():
	print("hello")
	disp()
	
print("before recursion")
disp()
print("after recursion")