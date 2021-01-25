import pandas as pd

s = pd.Series(list('abcde'),index=[0,3,2,5,10])
#s = pd.Series(list('abcde'),index=[0,3,2,5,2.2])
print(s.loc[3:5])
print(s.sort_index())
print(s.sort_index().loc[1:6])