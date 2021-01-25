import pandas as pd

df = pd.read_csv("apple.csv")
print(df.head(5))
print(type(df.Date[0]))

df = pd.read_csv("apple.csv",parse_dates=['Date'])
print(df.head(5))
print(type(df.Date[0]))

df = pd.read_csv("apple.csv",parse_dates=['Date'],index_col=0)
print(df.head(5))

print(df['2020-05'])
print(df['2020-05'].Close)

df1 = df.replace('[$]','',regex=True)
print(df1)
df1.to_csv("apple1.csv")