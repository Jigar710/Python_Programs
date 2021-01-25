a = 10
def outer():
	global a
	a =  100
	print(a)
	def inner():
		global a
		a = 1000
		print(a)
	inner()
	print(a)
	
print(a)
outer()
print(a)