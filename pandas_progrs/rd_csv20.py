import pandas as pd
df = pd.DataFrame({
	'score':['exceptional','avg','good','poor','avg','exceptional'],
	'student':['std1','std2','std3','std4','std5','std6']})
print(df)

new_df = df.replace(['exceptional','avg','good','poor'],[1,2,3,4])
print(new_df)