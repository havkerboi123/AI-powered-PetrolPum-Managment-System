import mysql.connector

mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="muhammad2003"
   
)

c = mydb.cursor()
c.execute("CREATE DATABASE test")