f = open("data.txt")

print(f.tell())
print(f.read(2))
print(f.tell())
print(f.read(5))
print(f.tell())