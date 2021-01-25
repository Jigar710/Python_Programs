from matplotlib import pyplot as plt

exp_vals = [1400,600,300,410,250]
exp_labels = ['Home Rent','Food','Phone / Internet Bill','Car','Other Utilities']

#plt.axis('equal')
#plt.pie(exp_vals,labels=exp_labels,radius=1.5,autopct='%0.2f%%',explode=[0,0.3,0,0,0],shadow=True,startangle=45)
plt.pie(exp_vals,labels=exp_labels,radius=1.5,autopct='%0.2f%%',explode=[0,0.3,0,0,0],shadow=True)
plt.tight_layout()
plt.show()