import pandas as  pd

temp_df = pd.DataFrame({
	"city":["mumbai","delhi","banglore"],
	"temp":[32,23,45]
},index=[0,1,2])

event = pd.Series(["rain","snow","no event"])#,name="event")
print(event)
'''
#df = pd.concat([temp_df,event])
df = pd.concat([temp_df,event],axis=1)
print(df)
'''
temp_df['event'] = event
print(temp_df)