class first:
	def disp1(self):
		print("d1")
	def _disp2(self):
		print("d2")
	def __disp3(self):
		print("d3")

class sec(first):
	pass
	
s = sec()
s.disp1()
s._disp2()
s._first__disp3()
#s._sec__disp3() <== error