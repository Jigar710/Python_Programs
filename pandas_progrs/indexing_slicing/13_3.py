import pandas as pd
df3 = pd.DataFrame({'A': [1, 2, 3],
                     'B': [4, 5, 6],
                      'C': [7, 8, 9]})
  

print(df3.where(lambda x: x > 4, lambda x: x + 10))