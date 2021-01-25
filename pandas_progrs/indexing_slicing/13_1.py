import pandas as pd
import numpy as np

dates = pd.date_range('1/1/2000', periods=8)
#print(dates)

df = pd.DataFrame(np.random.randn(8, 4),index=dates, columns=['A', 'B', 'C', 'D'])
print(df)


print(df[df<0])
print(df.where(df<0))
#print(df.where(df<0,-df))