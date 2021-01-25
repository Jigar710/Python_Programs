#seek() : use to move the cursor in a file
'''
sytnax : 
	seek(offset[,where])
		where : 0 : beg of file (default)
			  : 1 : current position
			  : 2 : end of file
'''			  
#hello world
f = open("E:\\Coding\\Python\\6.file_handling\\programs\\data.txt",'rb')
f.seek(4)
print(f.read(1),f.tell())
f.seek(2,1)
print(f.read(1),f.tell())
f.seek(-1,2)
print(f.read(1).decode('UTF-8'),f.tell())