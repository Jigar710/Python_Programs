'''
1
12
123
1234
12345
1234
123
12
1
'''

for i in range(1,6):
	for j in range(1,i+1):
		print(j,end='')
	print()
for i in range(4,0,-1):
	for j in range(1,i+1):
		print(j,end='')
	print()