#query() method demo
import pandas as pd
import numpy as np

n = 10
df = pd.DataFrame(np.random.randint(n/2,size=(n,2)),columns=list('bc'))

print(df)
print("========================================")
print(df.query('index<b<c'))
print("========================================")