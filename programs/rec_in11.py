#indirect recursion

i = 1
def disp():
	global i
	print("hello")
	i = i + 3
	
	if(i<=15):
		show()
	print("bye from disp",i)
	
def show():
	global i
	print("hi")
	i = i + 2
	
	if(i<=10):
		disp()
	print("bye from show")
		
print("before recursion")
show()
print("after recursion")