#query() method demo
import pandas as pd
import numpy as np

n = 10
df = pd.DataFrame(np.random.rand(n,3),columns=list('abc'))
print(df)
print("========================================")
print(df[(df.a < df.b) & (df.b<df.c)])
print("========================================")
print(df.query('(a<b) & (b<c)'))
print("========================================")