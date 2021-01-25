#variable length keyword args
def test(**a):
	print(a,type(a))
	
test(name='aaa',age=23)
test(city='aaa',sal=2300)
test(city='aaa',sal=2300,name='as')
#test(city='aaa',sal=2300,sal=234)
