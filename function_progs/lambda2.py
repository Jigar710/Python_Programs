def double(x):
	return 2*x

lst = [i for i in range(1,11)]
print(lst)

#lst1 = list(map(double,lst))
lst1 = list(map(lambda a : 2 * a,lst))
print(lst1)