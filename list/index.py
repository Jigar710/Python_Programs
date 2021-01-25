'''
index() method will return index value of the given number 
and if number is not exists in list then throws ValueError
'''
lst1 = list(range(1,11))
print(lst1)

ind = lst1.index(10)
print(ind)
ind = lst1.index(100)
print(ind)