#function without name
#syntax:
#	lambda args : logic

def addition(a,b):
	return a+b
	
x = addition(10,20)
print(x)

s = lambda a,b : a+b
print(s(1,2))

a = lambda x,y : x>y
print(a(3,2))