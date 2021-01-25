try:
	a = int(input("Enter A : "))
	b = int(input("Enter B : "))

	c = a / b

	lst = [1,2,3]
	print(c,lst[c])
	
except Exception as e: #default except block
	print(e)#print(e.__str__())
	print(type(e))
	print(dir(e))
	#e.__cause__()
	print(e.__dict__)
	print(e.args)
print("bye bye")