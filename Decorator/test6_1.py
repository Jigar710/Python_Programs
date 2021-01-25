#print(globals.__doc__)

a = 10
def m1():
	b = 20
	print(globals())
	def m2():
		print("=======================")
		print(globals())
		print("=======================")
	m2()
m1()
#print(locals())