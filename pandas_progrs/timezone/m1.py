import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [51,50,52,48,47,49,46]

#plt.plot(x,y)
#plt.plot(x,y,color='green')
#plt.plot(x,y,color='green',linewidth=4)
#plt.plot(x,y,color='green',linewidth=4,linestyle='dotted')

plt.xlabel('day')
plt.ylabel('temp')
plt.title('weather')
plt.plot(x,y,color='green',linewidth=4,linestyle='dotted')

plt.show()