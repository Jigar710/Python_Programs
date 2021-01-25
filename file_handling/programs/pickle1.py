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

class test:
	def set(self,city):	
		self.city = city
	def disp(self):
		print(self.city)
		
e1 = Emp()
e1.set('surat1',10000)

t = test()
t.set("gujarat")

bin_emp = pickle.dumps(e1)
bin_test = pickle.dumps(t)

print(bin_emp)
print(bin_test)

e2 = pickle.loads(bin_emp)
t2 = pickle.loads(bin_test)

e2.disp()
t2.disp()