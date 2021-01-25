import pandas as pd
import sqlalchemy

df = pd.read_csv("customer.csv")
print(df)

df1 = df.rename(columns={'customer Name':'name','customer Phone':'phone_number'})
print(df1)


engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/pandas_db')
df1.to_sql(name='customers',con=engine,index=False,if_exists='append')