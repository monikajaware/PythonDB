# Write a program to accept category like "romance" and display list of books of that category 
import pymysql
con=pymysql.connect(host="buktult3uitjon7amj7n-mysql.services.clever-cloud.com",
user="umqwpl7tg0xdpbx6",
passwd="53IOY90xH96QLXCyhpcH",
database="buktult3uitjon7amj7n"
)
myCursor=con.cursor()
ca=input("enter category: ")
myCursor.execute("select *from books where category=%s" %ca)
print(myCursor.fetchall())
con.commit()
con.close()

