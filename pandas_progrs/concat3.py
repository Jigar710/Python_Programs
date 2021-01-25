import pandas as  pd

temp_df = pd.DataFrame({
	"city":["mumbai","delhi","banglore"],
	"temp":[32,23,45]
})

wind_df = pd.DataFrame({
	"city":["banglore","mumbai"],
	"speed":[7,66]
})

#df = pd.concat([temp_df,wind_df])
df = pd.concat([temp_df,wind_df],axis=1)
print(df)