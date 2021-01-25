import pandas as pd
df = pd.read_csv("data.csv")
print(df)
print(df.loc[0])

print(df['day'])
print(df.day)
print(type(df['day']))
