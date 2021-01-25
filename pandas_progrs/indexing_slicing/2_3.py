#DataFrame with numeric columns 
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),index=['a','b','c','d','e','f','g','h'])
print(df)

print(df.loc['a'])
print(df.loc[['a','c','b']])
print(df.loc['a':'f'])
print(df.loc['a':'f'][0])
print(df.loc['a':'f'][[0,1]])
print(df.loc['a':'f'][0])
print(df.loc['a':'f',0:3])