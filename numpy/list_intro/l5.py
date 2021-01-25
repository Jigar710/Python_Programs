'''
lst = []
for i in range(1,11):
	if i%2==0:
		lst.append(i)
'''

lst = [i for i in range(1,11) if i%2==0]		
print(lst)

