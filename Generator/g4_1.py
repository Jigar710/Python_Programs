import time
import random

names = ['aaa','bbb','ccc','ddd','eee']
langs = ['hindi','gujarati','english']

def method(n):
	
	for i in range(n):
		dct = {
			"id":i+1,
			"name":random.choice(names),
			"lang":random.choice(langs)
		}
		yield dct
	
	
#t1 = time.clock()
t1 = time.perf_counter()
lst = method(70000000)
#t2 = time.clock()
t2 = time.perf_counter()
print(t2-t1)
t3 = time.perf_counter()
next(lst)
t4 = time.perf_counter()
print(t4-t3)