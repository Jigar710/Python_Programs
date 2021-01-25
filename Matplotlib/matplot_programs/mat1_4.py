from matplotlib import pyplot as plt
import numpy as np

#print(plt.style.available)
plt.style.use('fivethirtyeight')
#plt.xkcd()

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_pos = np.arange(len(ages_x))		#<== updation
width = 0.25 						#<== updation

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.bar(x_pos-width, dev_y, color="#444444",label='All Devs ',width=width)
# Median Python Developer Salaries by Age
py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.bar(x_pos, py_dev_y, color="#008fd5",label='Python Devs',width=width)

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_pos+width, js_dev_y, color="#e5ae38",label='JS Devs ',width=width)


plt.xticks(ticks=x_pos,labels=ages_x)		

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')

plt.legend()

plt.tight_layout()

plt.show()