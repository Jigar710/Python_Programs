import pandas as pd
df = pd.read_csv("timezone.csv",header=1,parse_dates=['Date Time'],index_col=0)
print(df)
print(df.index)

df1 = df.tz_localize(tz='US/Eastern')
print(df1)
print(df1.index)

#df2 = df.tz_convert(tz='Europe/Berlin')
df2 = df.tz_localize(tz='Europe/Berlin')
print(df2)
print(df2.index)

df3 = df.tz_localize(tz='Asia/Calcutta')
print(df3)
print(df3.index)
df3.index = df3.index.tz_convert(tz='Europe/Berlin')
print(df3.index)