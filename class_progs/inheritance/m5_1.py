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
		first.disp(self)
		sec.disp(self)
		sec.disp1(self)
	
s = third()
s.disp()
