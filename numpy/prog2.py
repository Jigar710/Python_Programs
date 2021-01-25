import numpy as np

data = np.random.rand(2,3)

print(data)
print(type(data))
#print(help(data))
#print(dir(data))
print(data.shape)
print(data.ndim)
print(data.dtype)

print(data * 10)
print(data + data)
print(dir(data))

print(data.size)             # one element size
print(data.nbytes)          # whole array size