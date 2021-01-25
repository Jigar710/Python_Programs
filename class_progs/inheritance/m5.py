#method overriding with multiple inheritance
class first:
	def disp(cls):
		print("D1")
		
class sec:
	def disp(self):
		print("D2")
	def disp1(self):
		print("magic")
	
class third(first,sec):
	def disp(self):
		print("D3")
		super().disp()
		super().disp1()
	
s = third()
s.disp()

for i in third.__mro__:
	print(i)