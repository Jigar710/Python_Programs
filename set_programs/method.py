s = set()

lst = dir(s)

for i in lst:
	if '_' not in i:
		print(i)