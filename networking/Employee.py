class Emp:
	def __init__(self):
		self.name = ''
		self.age = 0
		self.sal = 0
	
	def set(self,name,age,sal):
		self.name = name
		self.age = age
		self.sal = sal
	
	def disp(self):
		print(self.name,self.age,self.sal)
		
	def getName(self):
		return self.name