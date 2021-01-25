lst = list(range(1,11))
print(lst)

print(lst.count(5))

lst[3:7] = [5,5,5,5]
print(lst)
print(lst.count(5))
print(lst.count(500))