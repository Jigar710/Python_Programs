#direct recursion

i = 1
def disp():
	global i
	print("hello")
	i = i + 1
	if(i<=5):
		disp()
	
print("before recursion")
disp()
print("after recursion")