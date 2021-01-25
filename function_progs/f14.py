def test(a,b,/,*,c,d):
	print(a,b,c,d)
	
test(1,2,d=10,c=23)
test(1,2,c=10,d=23)
#test(1,2,10,20) <== not allowed, last two args must be keyword args
#test(1,b=2,c=10,d=23) <== not allowed, bcoz b is a positional arg
