class Emp:
	def set(self,name,age,sal):
		self.name = name
		self.age = age
		self.sal = sal
		
	def disp(self):
		print(self.name,self.age,self.sal)
		
		
e1 = Emp()
e2 = Emp()

e1.set("aaa",10,10000)
e2.set(sal = 20000,name="bbb",age=20)

if(e1.sal > e2.sal):
	e1.disp()
else:
	e2.disp()