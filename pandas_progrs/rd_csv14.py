import pandas as pd

df = pd.read_csv("data.csv",parse_dates=['day'])
df.set_index('day',inplace=True)

new_df = df.dropna(how='all')
print(df)
print(new_df)