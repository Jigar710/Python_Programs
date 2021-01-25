a = {1,2,3,4,5}
b = {1,2,3}

print(b.issubset(a))
print(a.issubset(b))

print(b.issuperset(a))
print(a.issuperset(b))

print(a.isdisjoint(b))

a = {1,2,3}
b = {30}
print(a.isdisjoint(b))
