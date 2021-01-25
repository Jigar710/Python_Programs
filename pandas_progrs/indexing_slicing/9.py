import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(6, 4),index=list(range(0, 12, 2)),columns=list(range(0, 8, 2)))
print(df1)
print(df1.iloc[:3])
print(df1.iloc[1:5,2:4])
print(df1.iloc[[1,3,5],[1,3]])
print(df1.iloc[1:3,:])
print(df1.iloc[:,1:3])
print(df1.iloc[1,1])
print(df1.iloc[1])