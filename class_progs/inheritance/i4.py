class test:
	def disp1(self):
		print("d1")
	def _disp1(self):
		print("d2")
	def __disp1(self):
		print("d3")
		
		
t = test()

t.disp1()
t._disp1()
t._test__disp1()

lst = dir(t)
print(lst)