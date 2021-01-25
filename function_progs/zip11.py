d1 = {'a':1,'b':2,'c':3}
d2 = {'aa':10,'bb':22,'cc':33}

for i,j in zip(d1,d2):
	print(i," : ",j)
	
print("============================")
for i,j in zip(d1.items(),d2.items()):
	print(i," : ",j)
	
print("============================")
for (k1,v1),(k2,v2) in zip(d1.items(),d2.items()):
	print(k1,v1," : ",k2,v2)