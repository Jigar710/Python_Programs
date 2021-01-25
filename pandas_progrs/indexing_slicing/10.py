import pandas as pd

s = pd.Series(range(-3, 4))
print(s)
print(s[s>0])
print(s[(s<-1) | (s>0.5)])
print(s[~(s<0)])
