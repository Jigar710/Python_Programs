#variable length args
def test(*a):
	print(a,type(a))
	
test(10,20,30,40,50)
test(10,20)
test(10)
test()