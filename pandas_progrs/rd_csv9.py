import pandas as pd

df = pd.read_csv("data.csv",parse_dates=['day'])
df.set_index('day',inplace=True)

#new_df = df.fillna(method="bfill",axis=1)
new_df = df.fillna(method="ffill",axis="columns")

print(new_df)