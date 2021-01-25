import pandas as pd

y = pd.Period('2016',freq='Q-JAN')
print(y)
print(y.start_time)
print(y.end_time)

#Q4 : NOV ==> JAN