try:
	a = int(input("Enter A : "))
	b = int(input("Enter B : "))

	c = a / b

	lst = [1,2,3]
	print(c,lst[c])
except Exception as e:
	print(type(e))
	
print("bye bye")