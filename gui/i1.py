class First:
	def disp(self):
		print("A")
class Sec:
	def disp(self):
		print("B")
class Third(First,Sec):
	def disp(self):
		print("C")
		
t = Third()
t.disp()