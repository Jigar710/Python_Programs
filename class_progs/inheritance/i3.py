class test:
	def disp1(self):
		print("d1")
	def _disp2(self):
		print("d2")
	def __disp3(self):
		print("d3")
		

if(__name__=='__main__'):		
	t = test()

	t.disp1()
	t._disp2()
	t._test__disp3()

	lst = dir(t)
	print(lst)