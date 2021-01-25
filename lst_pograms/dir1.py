s = dir(list)

print(type(s))

print(s)

print()

for i in s:
	if '__' not in i:
		print(i)