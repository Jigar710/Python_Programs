t = tuple()

lst = dir(t)

for i in lst:
	if '_' not in i:
		print(i)