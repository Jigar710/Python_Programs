import time

def wrapper(func):
	start = time.time()
	func()
	end = time.time()
	print(func.__name__,(end-start)*1000)

def square():
	global lst
	result = []
	for i in lst:
		result.append(i ** 2)
	return result
	
def cube():
	global lst
	result = []
	for i in lst:
		result.append(i ** 3)
	return result
	
#lst = [1,2,3,4,5]
lst = list(range(1000000))
wrapper(square)
wrapper(cube)