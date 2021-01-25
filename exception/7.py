#except block with default except block
try:
	a = int(input("Enter A : "))
	b = int(input("Enter B : "))

	c = a / b

	lst = [1,2,3]
	print(c,lst[c])
except ValueError:
	print("Enter proper data")
except Exception as e: #default except block
	print("some problem ",e)
	
print("bye bye")