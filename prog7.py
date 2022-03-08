# Write a program to accept bookcode & new price and update book data in the table if found else display "book does not exist"   
import pymysql
con=pymysql.connect(host="buktult3uitjon7amj7n-mysql.services.clever-cloud.com",
user="umqwpl7tg0xdpbx6",
passwd="53IOY90xH96QLXCyhpcH",
database="buktult3uitjon7amj7n"
)
myCursor=con.cursor()
try:
    bc=int(input('enter book code: '))
    myCursor.execute("select *from books where bookcode=%d" %bc)
    data=myCursor.fetchall()
    if data:
        pri=int(input('enter price : '))
        myCursor.execute("update books set price=price+%d where bookcode=%d" %(pri,bc))
    else:
        print("book does not exist")
except:
    print("error in updation")   
 
con.commit()
con.close()


   

