# Add new column "review varchar(500)" to the books table using alter query 
import pymysql
con=pymysql.connect(host="buktult3uitjon7amj7n-mysql.services.clever-cloud.com",
user="umqwpl7tg0xdpbx6",
passwd="53IOY90xH96QLXCyhpcH",
database="buktult3uitjon7amj7n"
)
myCursor=con.cursor()
myCursor.execute("alter table books add column review varchar(500)")
myCursor.fetchall() 

con.commit()
con.close()