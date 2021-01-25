lst = list(range(10,101,10))
print(lst)

lst = [i*10 for i in range(1,11)]
print(lst)

lst = []
for i in range(1,11):
	lst.append(i*10)
print(lst)

lst2 = []
for i in lst:
	lst2.append(2*i)
print(lst2)