from functools import reduce
def method(a,b):
	if a>b:
		return a
	else:
		return b

lst = [23,4,33,112,2]
m = reduce(method,lst)
print(m)