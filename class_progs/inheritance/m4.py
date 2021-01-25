#method overriding
class first:
	@classmethod
	def disp(cls):
		print("D1")
		
class sec(first):
	def disp(self):
		print("D2")
		super().disp()
		
	
s = sec()
s.disp()
