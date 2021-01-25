import numpy as np

arr = np.random.randn(4,3)
'''print(arr.mean(0))
demeaned = arr - arr.mean(0)
print(demeaned)
print(demeaned.mean(0))
'''
print(arr)
row_means = arr.mean(1)
print(row_means.shape)
row_means.reshape((4,1))
demeaned = arr - row_means.reshape((4,1))
print(demeaned.mean(1))
print(demeaned.mean(0))