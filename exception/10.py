#user defined exception class
class MyError(Exception):
	pass

try:
	a = int(input("Enter A : "))
	b = int(input("Enter B : "))

	if(a<0 or b<0):
		raise MyError("Hello error")
	c = a / b

	lst = [1,2,3]
	print(c,lst[c])
	
except Exception as e: #default except block
	print(type(e))
print("bye bye")