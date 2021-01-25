import pandas as pd

y = pd.Period('2016')
print(y)
#['2016','A-DEC']
print(y.start_time)
print(y.end_time)

lst = dir(y)
for i in lst:
	print(i)