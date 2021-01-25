try:
	a = int(input("Enter A : "))
	b = int(input("Enter B : "))

	if(a<0 or b<0):
		raise ValueError("negative value")
	c = a / b

	lst = [1,2,3]
	print(c,lst[c])
	
except Exception as e: #default except block
	e.a = 10
	print(e)#print(e.__str__())
	print(type(e))
	print(dir(e))
	#e.__cause__()
	print(e.__dict__)
	print(e.args)
print("bye bye")