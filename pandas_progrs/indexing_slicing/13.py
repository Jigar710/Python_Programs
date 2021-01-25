import pandas as pd
import numpy as np

s = pd.Series(np.arange(5), index=np.arange(5)[::-1], dtype='int64')
print(s)

print(s[s>0])
print(s.where(s>0))