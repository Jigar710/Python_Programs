class Test:
	def set(self):
		self.a = 10
	
t1 = Test()
t2 = Test()

t1.set()
t2.set()

print(t1.a)
print(t2.a)

t1.a = 99

print(t1.a)
print(t2.a)

t2.a = 999

print(t1.a)
print(t2.a)


