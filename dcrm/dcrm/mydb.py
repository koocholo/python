# install my sql on your computer
# http://dev.mysql.com/dowmloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install my sql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Mehdi80!'
)

# prepare a cursor object
cursorObject = dataBase.cursor()
# creat a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")
