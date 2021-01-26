import pandas as pd
import nsepy
from datetime import datetime,timedelta,date
import time 

start = time.time()
to_date = datetime.now()
to_date = datetime.strftime(to_date,"%y,%m,%d")
to_date = datetime.strptime(to_date,"%y,%m,%d")
print(to_date)
from_date = to_date - timedelta(days = 130)
df = nsepy.get_history(symbol = "RELIANCE",start= from_date,end=to_date)
print(df)
end = time.time()
print(end-start)
help(nsepy.get_history)


