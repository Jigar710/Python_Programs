import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:@localhost:3306/pandas_db_1")
#df = pd.read_sql_table("customers",engine,columns=['name','phone_number'])
df = pd.read_sql_table("customers",engine)
print(df)

q = '''select c.name,c.phone_number,o.item_name,o.amount from customers as c 
	inner join orders as o on (c.id = o.customer_id)'''
df = pd.read_sql_query(q,engine)
print(df)
