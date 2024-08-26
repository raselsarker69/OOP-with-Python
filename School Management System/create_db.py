import pymysql

connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "password"
)

query = "CREATE DATABASE SCHOOL"

cursor = connection.cursor()

cursor.execute(query)