import time

def outer(func):
	def inner():
		start = time.time()
		c = func()
		end = time.time()
		print(func.__name__,(end-start)*1000,"ms")
	return inner
	
@outer
def square():
	global lst
	result = []
	for i in lst:
		result.append(i ** 2)
	return result

@outer	
def cube():
	global lst
	result = []
	for i in lst:
		result.append(i ** 3)
	return result
	
lst = list(range(1000000))
square()
cube()