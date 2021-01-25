lst = []
n = int(input("Enter limit : "))

try:
	for i in range(0,n):
		x = int(input("Enter data : "))
		lst.append(x)
except:
	print("Enter int nnumber")
		
print(lst)