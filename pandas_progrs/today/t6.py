import pandas as pd
df = pd.read_csv("data.csv")
print(df)
df.set_index('day',inplace=True)
#df = df.dropna()
df1 = df.dropna(thresh=1)
df2 = df.dropna(thresh=2)
df3 = df.dropna(thresh=3)
#df = df.dropna(how='all')
print(df1)
print(df2)
print(df3)