#indirect recursion

i = 1
def disp():
	global i
	print("hello")
	i = i + 1
	
	if(i<=5):
		disp()
	print("bye from disp")
	
def show():
	global i
	print("hi")
	i = i + 1
	
	if(i<=10):
		disp()
	print("bye from show")
		
print("before recursion")
show()
print("after recursion")