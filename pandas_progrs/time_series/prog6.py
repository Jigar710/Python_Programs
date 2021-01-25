import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

df = pd.read_csv("apple2.csv")
print(df.head())

rng = pd.date_range(start='7/1/2019',periods=22,freq='B')
print(rng)

usb = CustomBusinessDay(calendar = USFederalHolidayCalendar())

rng = pd.date_range(start='7/1/2019',periods=22,freq=usb)
print(rng)
