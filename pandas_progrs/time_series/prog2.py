import pandas as pd

df = pd.read_csv("apple1.csv",parse_dates=['Date'],index_col=0)
print(df.head())

print(df.loc['2020-05'])
print(df.loc['2020-05'].Close)
print(df.loc['2020-05'].Close.mean())
print(df.loc['2020-05-15'])
print(df.loc['2020-05-15':'2020-05-10'])
