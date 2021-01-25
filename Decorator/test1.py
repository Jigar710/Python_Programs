def m1():
	"""this is a sample method"""
	a,b = 10,20
	print(a,b)
	
print(type(m1))

lst = dir(m1)
#print(lst)

for i in lst:
	print(i)

print(m1.__class__)
print(m1.__code__)
print(m1.__dir__)
print(m1.__dict__)
print(m1.__doc__)