class A(Exception):
	def disp1(self):
		print("from A")
class B(A):
	def disp2(self):
		print("from B")
class C(B):
	def disp3(self):
		print("from C")


for i in (A,B,C):		
	try:
		raise i
	except C as c:		
		c.disp3()
	except B as b:		
		b.disp2()
	except A as a:		
		a.disp1()