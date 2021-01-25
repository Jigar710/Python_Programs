import pandas as pd
df = pd.read_csv("data.csv",parse_dates=['day'])
df.set_index('day',inplace=True)
print(df)

a = pd.date_range('2017-01-01','2017-01-11')
print(a)
