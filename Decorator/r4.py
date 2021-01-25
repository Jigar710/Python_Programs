from functools import reduce

lst = [23,4,33,112,2]
v = reduce(lambda a,b : a if(a>b) else b,lst)
print(v)

print(reduce.__doc__)