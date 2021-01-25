#wap for sum of elements passed from cmd line args

from sys import argv

#print(argv[1:])

#argv[1:] ==> ['10','20','30','hi','40','50']
s = 0
for i in argv[1:]:
	try:
		s = s + int(i)
	except:
		pass
print(s)

