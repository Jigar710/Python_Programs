import pandas as pd

df = pd.read_csv("data.csv",parse_dates=['day'])
print(df)
print(df.day[0])
print(type(df.day[0]))