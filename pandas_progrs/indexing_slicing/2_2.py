#char indexing in DataFrame
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),index=['a','b','c','d','e','f','g','h'], columns=['A', 'B', 'C', 'D'])
print(df)

print(df['C':])
print(df['A':'C'])
print(df.loc['a'])
print(df.loc[['a','c','b']])
print(df.loc['a':'f'])
print(df.loc['a':'f']['A'])
print(df.loc['a':'f'][['A','B']])
print("=====================================================")
print(df.loc['a':'f']['A':])
print(df.loc['a':'f','A':'C'])
print("=====================================================")