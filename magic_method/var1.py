class Emp:
	def __init__(self):
		self.var1 = "value1"
		self._var2 = "value2"
		self.__var3 = "value3"
		

e1 = Emp()
print(e1.__dict__)
print(e1.var1)
print(e1._var2)
print(e1._Emp__var3)