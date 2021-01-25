import pandas as pd
df = pd.read_csv("data.csv",parse_dates=['day'])
df.set_index('day',inplace=True)
#df = df.fillna(method='ffill')
#df = df.fillna(method='bfill')
#df = df.fillna(method='bfill',axis=1)
df = df.fillna(method='bfill',axis=1,limit=1)
print(df)