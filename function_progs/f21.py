
def test(a):
	print("hello")
def test():
	print("hi")
def test(a):
	print(a)
	
#test()
test(10)

'''
function overloading :
	more than one function with same name but diff args
		diff args
			diff seq 
			diff num
			diff types 
python does not support function overloading
but if user define more than one function with same name 
then PVM : python virtual machine
will consider latest defination only
'''