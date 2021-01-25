# multiple except block
try:
	a = int(input("Enter A : "))
	b = int(input("Enter B : "))

	c = a / b

	lst = [1,2,3]
	print(c,lst[c])
except (ValueError,ZeroDivisionError):
	print("Enter proper data")
except TypeError:
	print("iindex type must be int")

	
print("bye bye")