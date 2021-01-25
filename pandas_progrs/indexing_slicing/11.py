import pandas as pd
import numpy as np

df2 = pd.DataFrame({'a': ['one', 'one', 'two', 'three', 'two', 'one', 'six'],
	'b': ['x', 'y', 'y', 'x', 'y', 'x', 'x'],
    'c': np.random.randn(7)})
print(df2)
# only want 'two' or 'three'
criterion = df2['a'].map(lambda x: x.startswith('t'))

print(df2[criterion])

# equivalent but slower
print(df2[[x.startswith('t') for x in df2['a']]])

# Multiple criteria
print(df2[criterion & (df2['b'] == 'x')])

#with selection
print(df2.loc[criterion & (df2['b'] == 'x'), 'b':'c'])
'''
'''   