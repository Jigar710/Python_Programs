
lst1 = [1,2,5,3,1]
lst2 = [10,22,3,1,1]

#lst3 = list(map(lambda a,b:a>b ,lst1,lst2))
lst3 = list(map(lambda a,b:a if(a>b) else b ,lst1,lst2))
print(lst3)