class Emp:	
	pass
	
e1 = Emp()
e2 = Emp()

print(id(e1))
print(id(e2))

e3 = e1
print(id(e3))