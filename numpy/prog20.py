import numpy as np

arr = np.arange(15).reshape((3,5))
print(arr)
print(arr.T)

#print(arr.T*arr)
print(np.dot(arr.T,arr))
'''
arr:
1	2	3	4	5
6	7	8	9	10
11	12	13	14	15

arr.T
1	6	11
2	7	12	
3	8	13
4	9	14
5	10	15
'''