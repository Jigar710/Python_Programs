import pandas as pd

#df = pd.read_csv("timezone.csv")
df = pd.read_csv("timezone.csv",header=1,index_col='Date Time',parse_dates=True)
print(df)
print(df.index)

df = df.tz_localize(tz='US/Eastern')
print(df)
print(df.index)

df = df.tz_convert(tz='Europe/Berlin')
print(df)
print(df.index)

from pytz import all_timezones
print(all_timezones)