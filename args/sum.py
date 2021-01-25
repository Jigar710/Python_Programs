#wap for sum of elements passed from cmd line args

from sys import argv

#print(argv[1:])

try:
	s = 0
	for i in argv[1:]:
		s = s + int(i)
	print(s)
except:
	print("pass numeric values")