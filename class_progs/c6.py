class Emp:
	def get(self):
		self.name = input("Enter name : ")
		self.age = input("Enter age : ")
		self.sal = input("Enter sal : ")
		
	def disp(self):
		print(self.name,self.age,self.sal)

lst = list()

for i in range(3):
	print("Enter ",i,"th emp data : ",end="")
	e = Emp()
	e.get()
	lst.append(e)
	
print(lst)
for i in lst:
	i.disp()
	