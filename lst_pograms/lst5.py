lst = []
n = int(input("Enter limit : "))

for i in range(0,n):
	x = int(input("Enter data : "))
	lst.append(x)
	
c1 = c2 = 0

for i in range(0,len(lst)):
	if(lst[i]%2==0):
		c1+=1
	else:
		c2+=1
		
print("Even : ",c1)
print("Odd : ",c2)