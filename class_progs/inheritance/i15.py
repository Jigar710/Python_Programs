#hybrid
class first:
	def disp1(self):
		print("d1")
class sec:
	def disp2(self):
		print("d2")
class third(first,sec):
	def disp3(self):
		print("d3")
class fourth(third):
	def disp4(self):
		print("d4")
class fifth(third):
	def disp5(self):
		print("d5")
		
f = fourth()
f.disp1()
f.disp2()
f.disp3()
f.disp4()

z = fifth()
z.disp1()
z.disp2()
z.disp3()
z.disp5()