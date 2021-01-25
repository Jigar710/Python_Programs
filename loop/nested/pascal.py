'''
pascal triangle

1
11
121
1331
14641
'''
n = int(input("Enter row size : "))

lst = []
for i in range(0,n):
	temp = []
	for j in range(0,i+1):
		if(j==0 or i==j):
			temp.append(1)
		else:
			temp.append(lst[i-1][j] + lst[i-1][j-1])
	lst.append(temp)
	
print(lst)
			
for i in lst:
	for j in i:
		print(j,end=' ')
	print()