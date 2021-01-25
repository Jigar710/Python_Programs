import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/pandas_db')
df = pd.read_sql_table("customers",engine)
print(df)

#read particular columns data
#df1 = pd.read_sql_table("customers",engine,columns=['id','name'])
df1 = pd.read_sql("customers",engine,columns=['id','name'])
print(df1)

q = '''select customers.name,customers.phone_number,orders.name,orders.amount
		from customers inner join orders on (orders.customer_id = customers.id)'''
print(q)

#df2 = pd.read_sql_query(q,engine)
df2 = pd.read_sql(q,engine)
print(df2)	