class test:
	def __init__(self):
		self.a = 10
		self._a = 100
		self.__a = 1000
		

if(__name__=='__main__'):
	print(__name__)
	t = test()
	print(t.a)
	print(t._a)
	print(t._test__a)
	print(t.__dict__)
