class Emp:
	"""
		this is emp class 
		and i just dev for prac
	"""
	def __init__(self,name="no name",sal=0):
		self.name = name
		self.sal = sal
		
	def disp(self):
		"""
		use to disp data of object
		"""
		print(self.name,self.sal)
	
	def __gt__(self,e):
		if(self.sal > e.sal):
			return True
		else:
			return False
			
	def __str__(self):
		return self.name + " : " +str(self.sal)
		
e1 = Emp("aaa",100000)
e2 = Emp("bbb",20000)

if(e1>e2):
	print(e1)
else:
	print(e2)

print(e1.__dict__)	

'''	
help(Emp)
print(Emp.__doc__)
print(Emp.disp.__doc__)
help(Emp.disp)
'''