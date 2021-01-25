lst = list(range(1,11))
print(lst)

lst1 = []
'''
for i in lst:
	if(i%2==0):
		lst1.append(0)
	else:
		lst1.append(1)
'''
for i in lst:
	lst1.append(i%2)
print(lst1)

def evenorodd(n):
	'''if(n%2==0):
		return 0
	else:
		return 1
	'''
	return n%2
		
lst2 = list(map(evenorodd,lst))
print(lst2)


lst3 = list(map(lambda n : n%2,lst))
print(lst3)