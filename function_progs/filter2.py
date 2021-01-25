#filter method
#syntax
#	filter(method,iterator)
	

def evenOrOdd(x):
	if(x%2==0):
		return True
	else:	
		return False
		
lst = [i for i in range(1,11)]
print(lst)

lst1 = filter(evenOrOdd,lst)
print(lst1)
print(list(lst1))