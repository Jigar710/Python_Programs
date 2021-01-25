import time

def outer(func):
	def inner(lst):
		start = time.time()
		func(lst)
		end = time.time()
		print(func.__name__,(end-start)*1000,"ms")
	return inner
	
@outer
def square(lst):
	result = []
	for i in lst:
		result.append(i ** 2)
	return result

@outer
def cube(lst):
	result = []
	for i in lst:
		result.append(i ** 3)
	return result
	
lst = list(range(1000000))
square(lst)
cube(lst)
print(square.__name__)