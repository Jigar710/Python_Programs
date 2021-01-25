def test(a,b,/,x,y,*,c,d):
	print(a,b,x,y,c,d)
'''not allow	
def test1(*,a,/,b):
	print(a,b)
'''	
	
test(1,2,10,20,d=200,c=100)
test(1,2,y=20,x=10,d=200,c=100)