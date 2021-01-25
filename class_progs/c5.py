class Emp:
	def get(self):
		self.name = input("Enter name : ")
		self.age = input("Enter age : ")
		self.sal = input("Enter sal : ")
		
	def disp(self):
		print(self.name,self.age,self.sal)

e1 = Emp()
e2 = Emp()
e3 = Emp()

e1.get()
e2.get()
e3.get()

e1.disp()
e2.disp()
e3.disp()