'''
we need mysql-connector library in Python for SQL connection

pip install mysql-connector
'''
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="", passwd="")
