a = 10
def outer():
	global a
	a =  100
	print(a)
	def inner():
		nonlocal a
		print(a)
		a = 1000
		print(a)
	inner()
	print(a)
	
print(a)
outer()
print(a)
'''
10
100
100
1000
1000
1000
'''