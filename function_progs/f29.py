def test(a,b):
	return a+b
	
c = test(1,2)
print(c)

def test1(a,b):	#default returns None
	print(a+b)
	
c = test1(1,2)
print("ans : ",c)

def test2(a,b):
	return a+b,a-b,a*b,a/b,a//b	
	
x = test2(5,2)
print(x,type(x))

x,y,*z = test2(5,2)
print(x,y,z)

a = (1,1,1)
print(a,type(a))

p,q,*z = (1,2,3,4,5)
print(z)