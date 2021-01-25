a = 10
def outer():
	
	a =  100
	print(a)
	def inner():
		a = 1000
		print(a)
	print(a)
	
print(a)
outer()
print(a)