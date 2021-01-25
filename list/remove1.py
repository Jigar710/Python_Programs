lst = list()
print(help(lst.remove))

lst1 = list(range(1,11))
print(lst1)

lst1.append(5)
print(lst1)

print(lst1.remove(5))
print(lst1)
lst1.remove(5)	
print(lst1)
lst1.remove(5)	#ValueError
print(lst1)