#indirect recursion

i = 1
def disp():
	global i
	print("hello")
	i = i + 1
	
	if(i<=5):
		show()
		return
	print("bye from disp")
	
def show():
	global i
	print("hi")
	i = i + 1
	
	if(i<=5):
		disp()
		
print("before recursion")
#show()
disp()
print("after recursion")
'''
hello(2) 	hi(3)	 hello(4) 	 hi(5)		hello(6)bye from disp
disp() <==> show() <==> disp()  <==> show() <==> disp()
'''