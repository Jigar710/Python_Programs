import numpy as np

names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
#data = np.random.randn(7,4)
data = np.arange(1,29).reshape(7,4)

mask = (names=='Bob') | (names=='Will')
print(mask)
print(data[mask])

print(data<10)
data[(data>5) & (data<10)] = 0
print(data)

data[names != 'Joe'] = 7
print(data)