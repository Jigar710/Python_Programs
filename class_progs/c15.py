#object as an arg
class Emp:
	def set(self,name,age,sal):
		self.name = name
		self.age = age
		self.sal = sal
	def disp(self):
		print(self.name,self.age,self.sal)		
	def comp(self,t):
		if(self.sal > t.sal):
			self.disp()
		else:
			t.disp()
		
		
e1 = Emp()
e1.set("aaa",10,10000)
e2 = Emp()
e2.set("bbb",20,20000)

e1.comp(e2)