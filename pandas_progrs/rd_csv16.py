import pandas as pd

df = pd.read_csv("data.csv",parse_dates=['day'])
df.set_index('day',inplace=True)

dt = pd.date_range("01-01-2017","01-11-2017")
new_df = df.reindex(dt)

print(new_df)
print(df)