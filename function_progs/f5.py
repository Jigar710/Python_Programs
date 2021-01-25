#default arg
#def calc(p,r=10,n):		Syntax Error : non-def arg follows by def arg
def calc(p,n,r=10):
	c = (p * n * r)/100
	print("amount : ",c)

calc(10000,2)
calc(100000,2)
calc(1000,1)
calc(100000,4,9)