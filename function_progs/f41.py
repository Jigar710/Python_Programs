lst = dir(__builtins__)
for i in lst:
	if '_' not in i:
		print(i)