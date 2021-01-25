lst = []
n = int(input("Enter limit : "))

for i in range(0,n):
	try:
		x = int(input("Enter data : "))
		lst.append(x)
	except:
		print("Enter int nnumber")
		
print(lst)