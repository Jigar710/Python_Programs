class first:
	def disp1(self):
		print("d1")
class sec(first):
	def disp2(self):
		print("d2")
class third(first):
	def disp3(self):
		print("d3")
		
s = sec()
s.disp1()
s.disp2()

t = third()
t.disp1()
t.disp3()