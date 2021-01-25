from functools import reduce

lst = [1,2,3,4,5]
v = reduce(lambda a,b:a+b,lst)
print(v)