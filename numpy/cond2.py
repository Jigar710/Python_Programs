import numpy as np

xarr = np.array([1,1.2,1.3,1])
yarr = np.array([2,2,2.3,2])
cond = np.array([True,False,True,True])

ans = np.where(cond,xarr,yarr)
print(ans)