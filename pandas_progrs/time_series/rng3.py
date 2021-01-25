import pandas as pd
from pandas.tseries.offsets import CustomBusinessDay

#myf = CustomBusinessDay(holidays=['2017-01-26'])
myf = CustomBusinessDay(holidays=['2017-01-26'],weekmask='Sat Sun')

rng = pd.date_range(start='1/1/2017',end='1/31/2017',freq=myf)
print(rng)   


