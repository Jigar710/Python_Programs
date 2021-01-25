import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),index=range(10,81,10), columns=['A', 'B', 'C', 'D'])
print(df)

print(df[['A','B']])
print(df.loc[[10,20]])
print(df.iloc[[0,1]])
