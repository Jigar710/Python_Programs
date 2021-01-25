#variable length args
def test(*a):
	print(a)
	
test(10,20)
test([10,20,30])
test(*[10,20,30])
test({'a':10,'b':20,'c':30})
test(*{'a':10,'b':20,'c':30})

#a,b,c = *[10,20,30] # not allowed
#x,y,z = *{'a':10,'b':20,'c':30} #not allowed

x,y,z = {'a':10,'b':20,'c':30}
print(x,y,z)	#<= disp keys
