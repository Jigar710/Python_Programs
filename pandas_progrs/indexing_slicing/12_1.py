import pandas as pd
import numpy as np

df = pd.DataFrame({'vals': [1, 2, 3, 4], 'ids': ['a', 'b', 'f', 'n'],
						'ids2': ['a', 3, 'c', 'n']})
print(df)
print("=====================================")
values = ['a','b',1,3]
print(df.isin(values))
print("=====================================")
values = {'ids': ['a', 'b'], 'vals': [1, 3]}
print(df.isin(values))
print("=====================================")
values = {'ids': ['a', 'b'], 'ids2': ['a', 'c'], 'vals': [1, 3]}
row_mask = df.isin(values)
row_mask = row_mask.all(1)

print("=====================================")
print(row_mask)
print(df[row_mask])