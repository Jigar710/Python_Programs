'''
equ = "(x+1)*(x+1)"
x = 4
ans = eval(equ)
print(ans)
'''

'''
data = {}
equ = "(x+1)*(x+1)"
y = 4
data['x'] = y
ans = eval(equ,None,data)
print(ans)
'''
data={}
y = 4
data['x'] = y
def method():
	equ = "(x+1)*(x+1)"
	ans = eval(equ,data)
	print(ans)

method()