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

f = open(r"E:\Coding\Python\6.file_handling\programs\emp1.txt","r")
e = json.load(f)
print(e)
print(type(e))
f.close()