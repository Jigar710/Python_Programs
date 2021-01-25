'''
global variable : common between all function
local variable : local to function
'''

a = 10

def f1():
	global a
	a = 100
	print("f1 : ",a)
	
def f2():
	print("f2 : ",a)
	
print(a)
f1()
f2()
print(a)