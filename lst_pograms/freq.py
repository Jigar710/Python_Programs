lst = [2,3,22,3,2,2,3]
f = []
num = []

for i in lst:
	if i not in num :
		c = lst.count(i)
		f.append(c)
		num.append(i)
	
for i in range(0,len(f)):
	print(f[i],num[i])

'''	
sum()
max()
min()
count()
'''