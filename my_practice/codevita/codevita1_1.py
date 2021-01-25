n, k = input().split()
n, k = int(n), int(k)
lst1 = list(map(int,input().split()))[:n]

m = max(lst1)
effort = 0
index = lst1.index(m)
'''
#first idea
for i in range(len(lst1)-1):
	if(i!=k-1):
		for j in range(i+1,len(lst1)):
			if(lst1[i] > lst1[j]):
				
				effort += lst1[i] * lst1[j]
				lst1[i],lst1[j] = lst1[j],lst1[i]
	else:
		lst1[k-1],lst1[index] = lst1[index],lst1[k-1]
		effort += lst1[index]*lst1[k-1]


print(lst1,effort)
'''
#updated logic
min_value = min(lst1)
min_value_index = lst1.index(min_value)
max_value = max(lst1)
max_value_index = lst1.index(max_value)

for i in range(len(lst1)-1):
	if(i!=k-1):
		for j in range(i+1,len(lst1)):
			if(lst1[i] > lst1[j]):
				
				if(lst1[i]==min_value or lst1[j]==min_value):
					effort += lst1[i] * lst1[j]
					lst1[i],lst1[j] = lst1[j],lst1[i]
					min_value_index = i
					
				else:
					
					effort += lst1[min_value_index] * lst1[j]
					lst1[min_value_index],lst1[j] = lst1[j],lst1[min_value_index]
					
					effort += lst1[i] * lst1[j]
					lst1[i],lst1[j] = lst1[j],lst1[i]
					
					effort += lst1[i] * lst1[min_value_index]
					lst1[i],lst1[min_value_index] = lst1[min_value_index],lst1[i]
					
	else:
		if(lst1[k-1]==min_value or lst1[max_value_index]==min_value):
			effort += lst1[k-1] * lst1[max_value_index]
			lst1[k-1],lst1[max_value_index] = lst1[max_value_index],lst1[k-1]
		else:

			effort += lst1[min_value_index] * lst1[k-1]
			lst1[min_value_index],lst1[k-1] = lst1[k-1],lst1[min_value_index]
			
			effort += lst1[max_value_index] * lst1[k-1]
			lst1[max_value_index],lst1[k-1] = lst1[k-1],lst1[max_value_index]
			
			effort += lst1[max_value_index] * lst1[min_value_index]
			lst1[max_value_index],lst1[min_value_index] = lst1[min_value_index],lst1[max_value_index]
			
print(lst1,effort)