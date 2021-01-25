'''
global variable
	all the function can access,update those variables
'''
a = 10
b = 20

def m1():
	global a
	global b
	print("from m1 before updation : ",a,b)
	a += 1	#==>	a = a + 1
	print("from m1 after updation : ",a,b)
def m2():
	global a,b
	print("from m2 before updation : ",a,b)
	a *= 10
	print("from m2 after updation : ",a,b)
	
	
print("before function calling : ",a,b)
m1()
m2()
print("after function calling : ",a,b)