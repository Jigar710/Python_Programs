import pandas as pd

df = pd.read_csv("fb.csv")
#df = pd.read_csv("fb.csv",parse_dates=['Date'],index_col=0)
print(df)


df['1 day change'] = df['Price'].shift(1)
print(df)

print(df.index)
'''
df.index = df.index.tz_localize(tz='Europe/Berlin')
print(df.index)
'''
'''
df.index = pd.date_range(start='2017-08-15',periods=10,freq='B')
print(df.index)
#df = df.tshift(1)
df.index = df.index.shift(1)
print(df)
'''
df = df.shift(1)
print(df)
