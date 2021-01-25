import pandas as  pd
ind_wt = pd.DataFrame({
	"city":["mumbai","delhi","surat","pune"],
	"temp":[45,23,14,20],
	"humidity":[15,100,7,23]
})

us_wt = pd.DataFrame({
	"city":["mumbai","delhi","adi"],
	"temp":[25,26,12],
	"humidity":[155,110,172]
})

df = pd.merge(ind_wt,us_wt,on="city")
print(df)