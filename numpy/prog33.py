import numpy as np

arr = np.arange(10)


np.save('data/some_array',arr)

print(np.load('data/some_array.npy'))

np.savez('data/array_archive.npz',a=arr,b=arr)
arch = np.load('data/array_archive.npz')
print(arch['b'])

np.savez_compressed('data/array_compressed.npz',a = arr,b=arr)
