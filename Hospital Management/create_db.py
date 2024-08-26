import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password"
)

query="CREATE DATABASE HOSPITAL"

cursor=connection.cursor()

cursor.execute(query)