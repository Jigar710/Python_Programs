from pandas.tseries.holiday import AbstractHolidayCalendar,nearest_workday,Holiday
from pandas.tseries.offsets import CustomBusinessDay
import pandas as pd

class MyCalendar(AbstractHolidayCalendar):
    """
    US Federal Government Holiday Calendar based on rules specified by:
    https://www.opm.gov/policy-data-oversight/
       snow-dismissal-procedures/federal-holidays/
    """

    rules = [
        Holiday("New Years Day", month=1, day=26, observance=nearest_workday),
        ]
	
rng = pd.date_range(start="1/1/2020",end="31/1/2020",freq='B')
print(rng)

myc = MyCalendar()
myf = CustomBusinessDay(calendar=myc)
rng = pd.date_range(start="1/1/2020",end="31/1/2020",freq=myf)
print(rng)

