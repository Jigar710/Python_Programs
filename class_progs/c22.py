class Emp:
	def set(self,name,age,sal):
		self.name = name
		self.age = age
		self.sal = sal
	
	def disp(self):
		print(self.name,self.age,self.sal)
		
	def copy(self):
		e = Emp()
		e.name = self.name
		e.age = self.age
		e.sal = self.sal
		return e

e1 = Emp()
e2 = Emp()

e1.set("aaa",10,10000)

#e2 = e1
e2 = e1.copy()

e2.disp()