#method overriding
class first:
	def disp(self):
		print("D1")
		
class sec(first):
	def disp(self):
		print("D2")
		
	
s = sec()
s.disp()