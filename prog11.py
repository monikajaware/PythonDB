# Write a program to accept bookcode and review, update the record with the review contents 
import pymysql
con=pymysql.connect(host="buktult3uitjon7amj7n-mysql.services.clever-cloud.com",
user="umqwpl7tg0xdpbx6",
passwd="53IOY90xH96QLXCyhpcH",
database="buktult3uitjon7amj7n"
)
myCursor=con.cursor()
bc=int(input("enter bookcode: "))
riv=input("enter review: ")
myCursor.execute("UPDATE books set review=%s where bookcode=%d" %(riv,bc))
myCursor.fetchall()
print("record updated")
con.commit()
con.close()
