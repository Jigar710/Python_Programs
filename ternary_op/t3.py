#[False_Stat,True_Stat][cond]

a,b = 10,20
#c = [b,a][a>b]
c = (b,a)[a>b]
print(c)

#c = {False:b,True:a}[a>b]
c = {True:a,False:b}[a>b]
print(c)