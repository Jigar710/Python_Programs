'''
global variable
	all the function can access,update those variables
'''
a = 10
def m1():
	global a
	print("from m1 before updation : ",a)
	a += 1	#==>	a = a + 1
	print("from m1 after updation : ",a)
def m2():
	print("from m2 before updation : ",a)
	#a *= 10
	print("from m2 after updation : ",a)
	
	
print("before function calling : ",a)
m1()
m2()
print("after function calling : ",a)