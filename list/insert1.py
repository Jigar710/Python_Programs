'''
insert : use to insert a given data on a given position

if given +ve position is out of range then wil be consider as a len of list
and if given -ve position is out of range then wil be consider as a 0 index value
'''
lst1 = list(range(1,11))
print(lst1)

#lst1.insert(3,999)
lst1.insert(3,[99,9])
print(lst1)

lst1.insert(-1,990)
print(lst1)

lst1.insert(50,9)
print(lst1)

lst1.insert(-50,9)
print(lst1)
