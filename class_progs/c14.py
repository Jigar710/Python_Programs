class Emp:	
	def set(self,a):
		self.a = a
	def disp(self):
		print(self.a)
	
e1 = Emp()
e2 = Emp()

e1.set(10)
e2.set(100)

e1.disp()
e2.disp()

print(id(e1))
print(id(e2))

e3 = e1

print(id(e1))
print(id(e3))

e1.a = 99

e1.disp()
e3.disp()
