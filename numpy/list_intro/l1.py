lst = [1,2,3]
print(lst,type(lst))

lst = [1,2,3,2,3,3,1,2]
print(lst,type(lst))

lst = []
print(lst,type(lst))

lst = list()
print(lst,type(lst))

lst = [1,2.3,"hello",'welcome',[20,3]]
print(lst,type(lst))

for i in lst:
	print(i)
print("===============================")
#for i in range(0,len(lst)):
for i in range(len(lst)):
	print(lst[i])
print("===============================")	
i = 0
while i<len(lst):
	print(lst[i])
	i = i + 1