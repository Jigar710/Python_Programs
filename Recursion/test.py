#1	10	2	20	3	30	4	40	5	50

i = 1
a = 1
def disp():
	global a,i
	print(a,end=' ')
	a = a + 1
	i = i + 1
	if(i<=10):
		show()
	
b = 10
def show():
	global b,i
	print(b,end=' ')
	b = b + 10
	i = i + 1
	if(i<=10):
		disp()
	
disp()