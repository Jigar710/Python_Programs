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
		
		
f = open("emp.txt","rb")
e1 = pickle.load(f)
e2 = pickle.load(f)
e3 = pickle.load(f)
#print(type(e))
e1.disp()
e2.disp()
e3.disp()