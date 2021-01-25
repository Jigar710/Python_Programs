#query() method demo
#if column and index having same name

import pandas as pd
import numpy as np

n = 10

df = pd.DataFrame({'a': np.random.randint(5, size=5)})

print(df)
print("========================================")
print(df.query('a>2'))
print("========================================")
print(df.query('index>2'))