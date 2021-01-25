#forcing a positional args : use to declare positional only args
def test(a,b,c,d,/):
	print(a,b,c,d)

	
test(1,2,3,4)
test(1,2,3,4)
test(a=1,b=2,c=3,d=4)