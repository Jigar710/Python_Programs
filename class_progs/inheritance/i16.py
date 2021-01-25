class first:
	def __init__(self):
		print("first")
		
class sec(first):
	def __init__(self):
		print("sec")
		super().__init__()
		
s = sec()
		