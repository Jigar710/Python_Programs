#keyword args with def values
#def test(*,a,b,c=10):	
def test(*,a,b=99,c):	
	print(a,b,c)
	
test(a=10,b=20,c=100)
test(a=10,c=20)
	