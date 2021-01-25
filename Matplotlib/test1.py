from matplotlib import  pyplot as plt

days = [1,2,3,4,5,6,7]
max_t = [50,52,51,48,47,49,46]
min_t = [43,42,40,44,43,35,37]
avg_t = [45,48,48,46,40,42,41]

#plt.bar(days,max_t)
plt.bar(days,min_t)
plt.bar(days,avg_t,animated=True)

plt.grid(color='green')

plt.show()