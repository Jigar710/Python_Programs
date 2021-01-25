import time
class Database:
	def __init__(self):
		self.value = 100
		
	def update(self,amount):
		copy = self.value
		copy += amount
		time.sleep(2)
		self.value = copy
		print("success")
	
	def disp(self):
		print(self.value)
		
d = Database()
d.disp()
d.update(10)
d.disp()
		
		