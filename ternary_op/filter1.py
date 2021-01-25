lst = list(range(1,11))
print(lst)

lst1 = []
'''
for i in lst:
	if(i%2!=0):
		lst1.append(i)
'''

def evenorodd(n):
	if(n%2!=0):
		return True
	else:
		return False
	
lst2 = list(filter(evenorodd,lst))
print(lst2)