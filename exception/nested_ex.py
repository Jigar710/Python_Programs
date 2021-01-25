try:
	print("welcome to outer try")
	a = int(input("Enter A : "))
	b = int(input("Enter B : "))
	
	try:
		print("welcome to inner try")
		c = a / b
		print("ans : ",c)
		print("bye from inner try")
		
	except ZeroDivisionError:
		print("cant divide by zero")
	
	print("bye from outer try")
except ValueError:
	print("wrong input")
	
print("Good bye")