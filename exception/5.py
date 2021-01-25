# multiple except block
try:
	a = int(input("Enter A : "))
	b = int(input("Enter B : "))

	c = int(a / b)
	lst = [11,21,31]
	print(c,lst[c])
except ValueError:
	print("plz enter int value")
except TypeError:
	print("iindex type must be int")
except ZeroDivisionError:
	print("cant divide by zero")
	
print("bye bye")