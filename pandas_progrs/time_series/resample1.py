import pandas as pd

df = pd.read_csv("apple1.csv",parse_dates=['Date'],index_col=0)
print(df.Close.resample('M').mean())
print(df.Close.resample('W').mean())
print(df.Close.resample('Q').mean())
print(df.resample('M').mean())
