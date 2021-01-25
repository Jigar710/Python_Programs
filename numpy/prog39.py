import numpy as np

#arr = np.random.randn(5,2)
arr = np.arange(10).reshape(5,2)
print(arr)

#first,sec,third = np.split(arr,[1,3])
first,sec,third,fourth = np.split(arr,[1,2,3],axis=0)	#default value of axis is 0
#first,sec,third,fourth = np.split(arr,[1,2,3],axis=1)

print(first)
print(sec)
print(third)
print(fourth)