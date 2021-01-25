#filter method

def evenOrOdd(x):
	if(x%2==0):
		return True
	else:	
		return False
		
lst = [i for i in range(1,11)]
print(lst)

lst1 = []
for i in lst:
	if evenOrOdd(i)==True:
		lst1.append(i)
		
print(lst1)