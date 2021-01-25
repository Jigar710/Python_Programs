class first:
	def disp1(self):
		print("d1")
class sec(first):
	def disp2(self):
		print("d2")
class third(sec):
	def disp3(self):
		print("d3")
		
s = third()
s.disp1()
s.disp2()
s.disp3()