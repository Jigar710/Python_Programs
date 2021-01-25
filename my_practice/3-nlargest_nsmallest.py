import heapq

nums = [1,8,2,23,7,-4,18,23,42,37,2]
print(heapq.nlargest(3,nums))      #prints [42, 37, 23]
print(heapq.nsmallest(3,nums))     #prints [-4, 1, 2]

students = [
    {'name':'jigar','id':'101','age': '20'},
    {'name':'smit','id':'102','age': '21'},
    {'name':'nilesh','id':'301','age': '40'},
    {'name':'nandeep','id':'201','age': '23'},
]

cheap = heapq.nsmallest(2,students,key=lambda s:s['id'])
expensive = heapq.nlargest(2,students,key=lambda s:s['id'])

print(cheap)
print(expensive)
