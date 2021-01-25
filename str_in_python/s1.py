s = str()
#s = ''
#help(s)
for i in dir(s):
	if '_' not in i:
		print(i)