import numpy as np

xarr = np.array([1,1.2,1.3,1])
yarr = np.array([2,2,2.3,2])
cond = np.array([True,False,True,True])

print(xarr)
print(yarr)
print(cond)

ans = [(i if k else j) for i,j,k in zip(xarr,yarr,cond)]
print(ans)