class Test:
	def __init__(self,a = 10):
		self.a = a
		print("init")
	def __str__(self):
		return "oye this is str method"
		
t = Test()
print(type(Test))
print(type(t))
print(t.a)

'''
from TestEx import Demo
t1 = Demo()
print(type(t1))
'''