#replace even numbers by 0 
def check(n):
	if(n%2==0):
		return 0
	else:
		return n
		
lst = list(range(1,11))
print(lst)

lst1 = list(map(check,lst))
print(lst1)

lst2 = list(map(lambda n : 0 if(n%2==0) else n ,lst))
print(lst2)

lst3 = list(map(lambda n : -n if(n%2==0) else n,lst))
print(lst3)