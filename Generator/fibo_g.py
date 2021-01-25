#0 1 1 2 3 5...
# fibonacci series
def fibo(n):
	a,b = 0,1
	yield a
	yield b
	i = 2
	while(i<n):
		c = a + b
		yield c
		a,b = b,c
		i = i + 1
	
		
lst = fibo(7)
#print(lst)
for i in lst:
	print(i,end=' ')