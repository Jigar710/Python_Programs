#f = open("data.txt")#default mode is read
#f = open("data.txt","r")#default mode is read
#default mode is read
f = open("E:\\Coding\\Python\\6.file_handling\\programs\\file1.py")
if(f==None):
	print("file does not exists")
else:
	'''
	print(type(f))
	print(dir(f))
	'''
	print(f.name)
	print(f.mode)
	print(f.readable())
	print(f.writable())
	#print(f.read())
	#print(f.read(10))
	#print(f.readline())
	'''
	lst = f.readlines()
	print(lst)
	for line in lst:
		print(line,end='')
	'''
	print(f.read(5))
	print(f.readline())
	f.close()
	'''
	with open('file1.py') as f:
		print(f.read(5))
		print(f.readline())
	'''
