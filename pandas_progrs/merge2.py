import pandas as  pd
ind_wt = pd.DataFrame({
	"city":["mumbai","delhi","surat","pune"],
	"temp":[45,23,14,20],
})

us_wt = pd.DataFrame({
	"city":["mumbai","delhi","adi"],
	"humidity":[55,10,72]
})

df = pd.merge(ind_wt,us_wt,on="city")
print(df)