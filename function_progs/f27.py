#keyword variable length args
def test(name,**a):
	print(name)
	print(a)
	print("===============================")
	
test(name='surat',age=20)
test(name='surat')
test({'name':'surat','age':55})
test(**{'name':'surat','age':55})
#test(*{'name':'surat','age':55}) not allows

	
