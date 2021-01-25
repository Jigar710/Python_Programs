#forcing keywords args : use to force to set keywords args followed by *
def test(*,a,b,c,d):
	print(a,b,c,d)

test(d=4,c=3,b=2,a=1)
test(1,2,3,4)