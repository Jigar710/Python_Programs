def wrapper(func):
	def inner():
		print("welcome from outer")	
		func()
		print("bye from outer")	
		
	return inner

@wrapper
def m2(a):
	print("inner")
	
m2() #=> wrapper(m2)