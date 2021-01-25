#lst = [i*i for i in range(1,10000001)]
lst = (i*i for i in range(1,1000000000000000001))
print(type(lst))
print(next(lst))
