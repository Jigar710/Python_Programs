#pip install mysql-connector
#pip3 install mysql-connector

import mysql.connector as db

con = db.connect(host="localhost",user="root",password="")
q = "create database python_db";

c = con.cursor()

c.execute(q)
