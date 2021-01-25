import pandas as pd

#df = pd.read_csv("fb.csv")
df = pd.read_csv("fb.csv",parse_dates=['Date'],index_col=0)
print(df)
print(df.index)

df = df.tshift(1)
print(df)
print(df.index)