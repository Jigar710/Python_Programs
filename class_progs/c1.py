class Email:
	def set(self,a):
		self.data = a 

	def disp(self):
		print(self.data)

	def __str__(self):
		return "This is a email"
		
e1 = Email()
e2 = Email()
e3 = Email()

e1.set("a@gmail.com")
e2.set("b@gmail.com")
e3.set("c@gmail.com")

e1.disp()
e2.disp()
e3.disp()
print(e1)
print(dir(Email))