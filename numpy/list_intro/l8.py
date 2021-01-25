lst = [i*10 for i in range(1,11)]
print(lst)
print(lst[0:5]) # 5 - 0
print(lst[:5])
print(lst[4:])
print(lst[:])
print(lst[1:5:2])
print(lst[:5:2])
print(lst[1::2])
print(lst[::2])

print("========================================")
print(lst[-1:-5]) # -5 - -1 = -4
print(lst[-1:-5:-1]) # -5 - -1 = -4
print(lst[-1::-1])
print(lst[:-7:-1])
print(lst[::-1])

print("========================================")
print(lst[1:-5])
print(lst[-9:7])
print(lst[-5:1:-1])
print(lst[7:-9:-1])