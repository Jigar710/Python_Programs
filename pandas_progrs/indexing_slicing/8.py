import pandas as pd
import numpy as np

s1 = pd.Series(np.random.randn(5), index=list(range(0, 10, 2)))
print(s1)
print(s1.iloc[:3])
s1.iloc[:3] = 0
print(s1)