#a = []
#a = list()
#a = [1,2]
#b = dir(a)
'''
b = dir(list)
print(type(b))
#print(b)

for i in b:
	if '__' not in i:
		print(i)
'''

for i in dir(list):
	if '_' not in i:
		print(i)
a = []
print(help(a.clear))
