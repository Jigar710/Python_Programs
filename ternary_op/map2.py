def mulby2(n):
	return 2*n
	
	
lst = [i*10 for i in range(1,11)]
print(lst)

lst2 = list(map(mulby2,lst))
print(lst2)

lst3 = list(map(lambda n : 2*n,lst))
print(lst3)