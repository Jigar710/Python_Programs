import numpy as np

arr = np.arange(5)
print(arr)
print(arr*4)

arr = np.random.randn(4,3)
t = arr.mean(0)
print(t,t.shape)
#demeaned = arr - t.reshape(1,3)
demeaned = arr - t
print(demeaned)
print(demeaned.mean(0))