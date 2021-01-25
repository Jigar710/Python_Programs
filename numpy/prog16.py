import numpy as np

#names = np.array(['Bob','Joe','Will','Bob','Wil','Joe','Joe'])
names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'],)

#print(names,names.dtype,names.itemsize,names.nbytes)

#data = np.random.randn(7,4)
data = np.arange(1,29).reshape(7,4)
#print(data,data.dtype)

a = names=='Bob'
print(a,a.dtype)
print(data[a])#prints first and fourth row
print(data[a,2:])
print(data[a,3])

b = names!='Bob'
print(b)

c = ~(names=='Bob')
print(c)


print(data[b])
print(data[c])
print(data[~(names=='Bob')])
print(data>3)