lst = list()
print(help(lst.pop))

lst1 = list(range(1,11))
print(lst1)

print(lst1.pop())
print(lst1)
print(lst1.pop(3))
print(lst1)

print(lst1.pop(-3))
print(lst1)
'''
#print(lst1.pop(-30))	#IndexError
print(lst1.pop(30))		#IndexError
print(lst1)
'''
lst1.clear()
print(lst1)
print(lst1.pop())		# IndexError