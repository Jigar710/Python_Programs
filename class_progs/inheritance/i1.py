class test:
	def __init__(self):
		self.a = 10
		self._b = 100
		self.__c = 1000
		
t = test()
print(t.a)
print(t._b)
print(t._test__c)
print(t.__dict__)
