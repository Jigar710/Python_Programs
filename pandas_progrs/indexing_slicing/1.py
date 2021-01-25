import pandas as pd
import numpy as np

dates = pd.date_range('1/1/2000', periods=8)
print(dates)

#df = pd.DataFrame(np.random.randn(8, 4),index=dates, columns=['A', 'B', 'C', 'D'])
df = pd.DataFrame(np.arange(1,33).reshape(8,4),index=dates, columns=['A', 'B', 'C', 'D'])
print(df)

#print(df[0])   #error
print(df.iloc[0])  #1stro
print(df.loc[dates[0]])  #1st row
#print(df[dates[0]])   #error


