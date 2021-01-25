import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [50,51,52,48,47,46,49]

#plt.plot(x,y)
#plt.plot(x,y,color='green')
#plt.plot(x,y,color='green',linewidth=4)
#plt.plot(x,y,color='green',linewidth=4,linestyle='dashed')
#plt.plot(x,y,color='green',linewidth=4,linestyle='dotted')
#plt.plot(x,y,color='green',linewidth=4,linestyle='dotted',marker='+')
#plt.plot(x,y,color='green',linewidth=4,linestyle='',marker='+')
#plt.plot(x,y,color='green',linewidth=4,linestyle='-.',marker='+')
#plt.plot(x,y,color='green',linewidth=4,linestyle='-.',marker='+',markersize=25)
plt.xlabel('day')
plt.ylabel('temp')
plt.title('weather')
plt.plot(x,y,color='green',linewidth=4,linestyle='-.',marker='+',markersize=25,alpha=0.2)
plt.show()