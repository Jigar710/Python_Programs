#0 1 1 2 3 5...
# fibonacci series
def fibo(n):
	lst = [0,1]
	i = 2
	while(i<n):
		a = lst[i-1] + lst[i-2]
		lst.append(a)
		i = i + 1
	return lst
		
lst = fibo(7)
#print(lst)
for i in lst:
	print(i,end=' ')