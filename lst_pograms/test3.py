
lst = []
n = int(input("Enter limit : "))

i = 0
while(i<n):
	try:
		x = int(input("Enter data : "))
		lst.append(x)
		i += 1
	except:
		print("Enter int nnumber")
'''		
s = 0
for i in range(0,len(lst)):
	s = s + lst[i]
	
print(s)

m = lst[0]
for i in range(0,len(lst)):
	if(lst[i]>m):
		m = lst[i]
	
print(m)
'''
print(max(lst))
print(sum(lst))
'''
home work
count freq of given number in a list
lst = [2,3,4,5,2,3,2]
2
3
4
5
'''