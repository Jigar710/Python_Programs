class Test:
	def __new__(self):
		print("new")
	
t = Test()
print(type(Test))
print(type(t))
print(t)

'''
def m1():
	pass
	
t = m1()
print(t)
'''