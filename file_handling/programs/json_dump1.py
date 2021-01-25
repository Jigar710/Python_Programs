import json
class Emp:	
	def __init__(self):
		self.name = ''
		self.sal = 0
	def set(self,name,sal):	
		self.name = name
		self.sal = sal
	def disp(self):
		print(self.name,self.sal)

e1 = Emp()
e1.set("surat",10000)

f = open("emp1.txt","w")
json.dump(e1.__dict__,f)
f.close()

#print(dir(e1))
#print(e1.__dict__)