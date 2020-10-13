import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="7392336"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE base_1013")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)