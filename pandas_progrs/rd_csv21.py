import pandas as pd

df = pd.read_csv("weather_by_cities.csv")
print(df)

g = df.groupby('city')
print(g)

for city, city_wd in g:
    print(city, city_wd)

print(g.get_group('mumbai'))
print(g.get_group('mumbai')['day'])
print(type(g.get_group('mumbai')))

print(g.max())
print(g.mean())
print(g.describe())
