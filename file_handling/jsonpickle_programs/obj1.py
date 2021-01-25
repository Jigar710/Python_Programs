import json
import jsonpickle
class Emp:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def disp(self):
		print(self.name,self.age)
		
e1 = Emp('aaa',123)
file = open(r'E:\Coding\Python\6.file_handling\json_programs\obj.txt','w')
data = jsonpickle.encode(e1)
print(type(data))
print(data)
json.dump(data,file)