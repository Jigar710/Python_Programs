#find the length of file
f = open("E:\\Coding\\Python\\6.file_handling\\programs\\data.txt",'rb')
f.seek(0,2)
print(f.tell())