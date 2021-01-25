class Emp:	
	def __init__(self):
		self.name = ''
		self.sal = 0
	def set(self,name,sal):	
		self.name = name
		self.sal = sal
	def disp(self):
		print(self.name,self.sal)
	def __str__(self):
		return self.name + " : "+str(self.sal)
e1 = Emp()
e1.set('surat',10000)

f = open("emp.txt","w")
f.write(e1.__str__())
f.close()