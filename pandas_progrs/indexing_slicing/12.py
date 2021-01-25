import pandas as pd
import numpy as np

s = pd.Series(np.arange(5), index=np.arange(5)[::-1], dtype='int64')
print(s)

print(s.isin([2,4,6]))        #list and set arg
print(s[s.isin([2,4,6])])
print(s[s.index.isin([2, 4, 6])])
print(s.index)
'''

'''