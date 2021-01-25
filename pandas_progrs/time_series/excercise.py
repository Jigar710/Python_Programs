import pandas as pd

df = pd.read_csv("walmart.csv")
print(df)


df.set_index('Line Item',inplace=True)
print(df)

df = df.T
print(df)

df.index = pd.PeriodIndex(df.index,freq='Q-JAN')
print(df)

#df['start-date'] = df.index.start_time
df['start-date'] = df.index.map(lambda x : x.start_time)
df['end-date'] = df.index.map(lambda x : x.end_time)
print(df)