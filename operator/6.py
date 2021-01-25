a = 5
b = 5

print(id(a))
print(id(b))

if a is b:		
	print("yes")
else:
	print("no")

	
lst1 = [1,2,3]
lst2 = [1,2,3]
print(id(lst1))
print(id(lst2))
if lst1 is lst2:
	print("yes")
else:	
	print("no")