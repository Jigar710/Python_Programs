import pandas as pd

df = pd.read_csv("apple1.csv")
print(df.head(5))
print(type(df.Date[0]))

df = pd.read_csv("apple1.csv",parse_dates=['Date'])
print(df.head(5))
print(type(df.Date[0]))

df = pd.read_csv("apple1.csv",parse_dates=['Date'],index_col=0)
print(df.head(5))

print(df['2020-05'])
print(df['2020-05'].Close)
print(df['2020-05'].Close.mean())
print(df['2020-05-08':'2020-05-01'].Close)
