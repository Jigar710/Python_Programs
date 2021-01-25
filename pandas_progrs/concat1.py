import pandas as  pd
ind_wt = pd.DataFrame({
	"city":["mumbai","delhi","surat"],
	"temp":[45,23,14],
	"humidity":[80,60,70]
})
print(ind_wt)

us_wt = pd.DataFrame({
	"city":["new york","chicago","orlando"],
	"temp":[15,33,40],
	"humidity":[55,10,72]
})
print(us_wt)

print(pd.concat([ind_wt,us_wt]))
print(pd.concat([ind_wt,us_wt],ignore_index=True))
df = pd.concat([ind_wt,us_wt],keys=['India','US'])
print(df)
print(df.loc['US'])
