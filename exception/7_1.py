#except block with default except block
try:
	a = int(input("Enter A : "))
	b = int(input("Enter B : "))

	c = a / b

	lst = [1,2,3]
	print(c,lst[c])
	
except Exception as e: #default except block
	print("some problem ",e)
except ValueError:
	print("Enter proper data")

print("bye bye")