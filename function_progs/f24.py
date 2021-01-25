#variable length arg with positional and / or keyword args
def test(x,*a):
	print("X : ",x)
	print("A : ",a)
	print("=========================")
	
test(10)
test(10,20,30,40)
test([10,20,30])
test(*[10,20,30])
test({'a':10,'b':20,'c':30})
test(*{'a':10,'b':20,'c':30})

#test(10,20,x=30)	not allows