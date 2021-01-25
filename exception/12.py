try:
	a = int(input("Enter A : "))
	print(a)
except Exception as e:
	print(e)
else:
	print("bye bye")
	

	
try:
	f = open("somefile.txt")
except Exception as e:
	print(e)
else:
	print(f.read())