import pandas as pd

dates = ['2017-01-01','jan 5,2015','01/01/2017','2017.01.01','2017/01/01']
dt1 = pd.to_datetime(dates)
print(dt1)

'''
US : mm/dd/yyyy
Europe : dd/mm/yyyy
'''

print(pd.to_datetime('5/1/2015'))#US format
print(pd.to_datetime('5/1/2015',dayfirst=True))

dates = ['2017-01-01','jan 5,2015','01/01/2017','2017.01.01','2017/01/01','aaa']
#dt1 = pd.to_datetime(dates,errors='ignore')
dt1 = pd.to_datetime(dates,errors='coerce')
print(dt1)
