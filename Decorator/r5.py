#reduce method
from functools import reduce
#print(reduce.__doc__)

def method(a,b):
	print(a,b)
	return a+b

lst = [1,2,3,4,5]
v = reduce(method,lst,100)
#v = reduce(method,lst)
print(v)