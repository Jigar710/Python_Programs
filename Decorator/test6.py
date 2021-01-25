#print(globals.__doc__)

a = 10
def m1():
	b = 20
	print(globals())
	
	
m1()
#print(locals())