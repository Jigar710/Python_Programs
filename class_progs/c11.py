# . : member access operator
class Emp:
	"""this is a sample class"""
	pass
	
e1 = Emp()
e2 = Emp()

print(e1)
print(e2)
print(e2.__str__())
'''
print(id(e1))
print(id(e2))
'''

lst = dir(e1)
for i in lst:
	print(i)
	
print(e1.__class__)
print(e1.__doc__)
print(e2.__str__())	#magic methods
