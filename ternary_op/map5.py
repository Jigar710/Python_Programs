
lst1 = list(range(10,101,10))
print(lst1)
lst2 = list(range(20,201,20))
print(lst2)

def add1(a,b):
	return a+b
	
lst3 = list(map(add1,lst1,lst2))
print(lst3)


lst4 = list(map(lambda a,b:a+b,lst1,lst2))
print(lst4)