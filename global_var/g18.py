a = 10
def outer():
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