import time
import random

names = ['aaa','bbb','ccc','ddd','eee']
langs = ['hindi','gujarati','english']

def method(n):
	lst = []
	for i in range(n):
		dct = {
			"id":i+1,
			"name":random.choice(names),
			"lang":random.choice(langs)
		}
		lst.append(dct)
	return lst
	
#t1 = time.clock()
t1 = time.perf_counter()
#lst = method(700000)
lst = method(1)
#t2 = time.clock()
t2 = time.perf_counter()
print(t2-t1)
'''
for i in lst:
	print(i)
'''