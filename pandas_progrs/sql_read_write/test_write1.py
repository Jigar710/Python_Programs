import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:@localhost:3306/pandas_db_1")
df = pd.read_csv("customer.csv")
print(df)

#df.to_sql(name="xyz",con=engine,index=False)
#df = df.rename(columns={'customer Name':'name','customer Phone':'phone_number'})
df.rename(columns={'customer Name':'name','customer Phone':'phone_number'},inplace=True)
print(df)

df.to_sql(name="customers",con=engine,index=False,if_exists='append')