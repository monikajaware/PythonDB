#list of all book
from unittest import result
import pymysql
con=pymysql.connect(host="buktult3uitjon7amj7n-mysql.services.clever-cloud.com",
user="umqwpl7tg0xdpbx6",
passwd="53IOY90xH96QLXCyhpcH",
database="buktult3uitjon7amj7n"
)
myCursor=con.cursor()
s="select *from books"
myCursor.execute(s)
result=myCursor.fetchall()
for rec in result:
    print(rec)
con.close()