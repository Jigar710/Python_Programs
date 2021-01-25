class Test:
	#a = 1000
	def set(self,a):
		self.a = a
		Test.a = 1000
	
t1 = Test()
t2 = Test()

t1.set(100)
t2.set(200)

print(t1.a)
print(t2.a)
print(Test.a)