#read_sql1.py
import pandas as pd
import sqlalchemy

#sqlalchemy.create_engine("dialect+driver://user_name:password@ip_address:port_num/db_name")
engine = sqlalchemy.create_engine("mysql+pymysql://root:@localhost:3306/pandas_db")
'''
#df = pd.read_sql("customers",engine)
df = pd.read_sql("select * from customers",engine)
print(df)
'''
'''
df = pd.read_sql_table("customers",engine)
print(df)
'''
q = 'select name from customers'
df = pd.read_sql_query(q,engine)
print(df)