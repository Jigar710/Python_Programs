import pandas as pd

df = pd.read_csv("data.csv")
print(df)
print(df.day[0])
print(type(df.day[0]))
print(type(df.temp[0]))