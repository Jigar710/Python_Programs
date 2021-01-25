class first:
	def __new__(self):
		print("first")
		
class sec(first):
	def __new__(self):
		print("sec")
		super().__new__(self)
		
s = sec()

