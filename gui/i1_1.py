class First:
	def disp(self):
		print("A")
		
class Sec:
	def disp(self):
		print("B")
		
#class Third(First,Sec):
class Third(Sec,First):
	def disp(self):
		print("C")
		super().disp()
		
t = Third()
t.disp()