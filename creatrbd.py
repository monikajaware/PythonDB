import mysql.connector

con=mysql.connector.connect(host='localhost',user='root',password='Ankitgul@29')
curs=con.cursor()

curs.execute("create database spider2")

con.close()
