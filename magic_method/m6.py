class Emp:
	def __init__(self,name="no name",sal=0):
		self.name = name
		self.sal = sal
		
		
e1 = Emp()
e2 = Emp()
print(e1.name,e1.sal)

print(e1.__dict__)
print(e2.__dict__)

e1.age = 20
print(e1.__dict__)
print(e2.__dict__)

e1.mobs = [111,222]
print(e1.__dict__)
print(e2.__dict__)
