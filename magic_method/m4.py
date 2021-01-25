class Emp:
	def __init__(self,name="no name",sal=0):
		self.name = name
		self.sal = sal
		
	def disp(self):
		print(self.name,self.sal)
	
	def __gt__(self,e):
		if(self.sal > e.sal):
			return True
		else:
			return False
			
e1 = Emp("aaa",100000)
e2 = Emp("bbb",20000)

if(e1>e2):
	e1.disp()
else:
	e2.disp()