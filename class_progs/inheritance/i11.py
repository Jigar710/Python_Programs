class first:
	def disp1(self):
		print("d1")
class sec(first):
	def disp2(self):
		print("d2")
		
		
s = sec()
s.disp1()
s.disp2()