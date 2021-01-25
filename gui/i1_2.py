class First:
	def disp1(self):
		print("A")
		
class Sec:
	def disp2(self):
		print("B")
		
#class Third(First,Sec):
class Third(Sec,First):
	def disp3(self):
		print("C")
		super().disp1()
		super().disp2()
		
t = Third()
t.disp3()
print(Third.mro())