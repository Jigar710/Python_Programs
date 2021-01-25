#variable length args
def test(**a):
	print(a,type(a))
'''	
test(10,20,30)
test()
test(10)
test(10,'hi')

test([10,20,30])
test((10,20,30))
test({10,20,30})
test({'a':10,'b':20,'c':30})'''
test(d=10,b=20,c=30)
