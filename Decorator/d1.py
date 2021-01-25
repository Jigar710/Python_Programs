import time

def square(lst):
	result = []
	start = time.time()
	for i in lst:
		result.append(i ** 2)
	
	end = time.time()
	print(square.__name__,(end-start) * 1000)
	
	return result
	
def cube(lst):
	result = []
	start = time.time()
	for i in lst:
		result.append(i ** 3)
	
	end = time.time()
	print(cube.__name__,(end-start) * 1000)
	return result
	
#lst = [1,2,3,4,5]
lst = list(range(1000000))
r1 = square(lst)
r2 = cube(lst)
