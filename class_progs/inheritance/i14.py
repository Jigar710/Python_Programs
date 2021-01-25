#multiple
class first:
	def disp1(self):
		print("d1")
class sec:
	def disp2(self):
		print("d2")
class third(first,sec):
	def disp3(self):
		print("d3")
		
t = third()
t.disp1()
t.disp2()
t.disp3()