#query() method demo
import pandas as pd
import numpy as np

n = 10
df = pd.DataFrame(np.random.randint(n/2,size=(n,2)),columns=list('bc'))
df.index.name = 'a'
print(df)
print("========================================")
print(df.query('(a<b) and (b<c)'))
print("========================================")