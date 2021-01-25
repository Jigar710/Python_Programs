import pickle #use for serialization
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
e2 = Emp()
e3 = Emp()
e1.set('surat1',10000)
e2.set('surat2',20000)
e3.set('surat3',30000)

f = open("emp.txt","wb")
#print(help(pickle.dump))
pickle.dump(e1,f)
pickle.dump(e2,f)
pickle.dump(e3,f)
f.close()