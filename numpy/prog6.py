import numpy as np

#[0 1 2 3 4 5 6 7 8 9]
arr = np.arange(10)

print(arr)

print(arr[5])

print(arr[5:8])

arr[5:8] = [12]
print(arr)

lst = [0,1,2,3,4,5,6,7,8,9]
print(lst[5])
print(lst[5:8])

lst[5:8] = [12]
print(lst)
