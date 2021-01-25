'''
global variable
	all the function can access,update those variables
'''
a = 10
def m1():
	print("from m1 : ",a)
def m2():
	print("from m2 : ",a)
	
print("before function calling : ",a)
m1()
m2()
print("after function calling : ",a)