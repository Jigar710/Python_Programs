#keyword variable length args
def test(**a):
	print(a)
	
test(name='surat',age=20)
test(name='surat')
#test(name='surat',20) not allowed
	
