import pandas as pd
from pandas.tseries.holiday import AbstractHolidayCalendar,Holiday,nearest_workday
from pandas.tseries.offsets import CustomBusinessDay


class INDHolidayCalendar(AbstractHolidayCalendar):
	rules = [
        Holiday("26th jan", month=1, day=25, observance=nearest_workday),
    ]

myf = CustomBusinessDay(calendar=INDHolidayCalendar())
#rng = pd.date_range(start='1/1/2017',end='1/31/2017',freq=myf)
rng = pd.date_range(start='1/1/2020',end='1/31/2020',freq=myf)
print(rng)