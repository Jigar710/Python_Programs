import numpy as np
'''
arr = np.arange(24).reshape((2,3,4))
print(arr)
print(arr.T)
'''
#2,3,2 => 2,3,2	==> a[i][j][k] : a[k][i][j]
#arr = np.arange(1,13).reshape((2,3,2))
#2,3,4 => 4,3,2	
arr = np.arange(1,25).reshape((2,3,4))
print(arr)
print("=====Transpose======")
print(arr.T)

print("=====Transpose method======")
print(arr.transpose((1,0,2)))	# 2,3,4 ==> 3,2,4

print(arr)

print(arr.swapaxes(1,2))	#=>	0,2,1
print(arr.swapaxes(1,0))	#=>	1,0,2
print(arr.swapaxes(2,0))	#=>	2,1,0
