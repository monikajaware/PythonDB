# Write a program to accept bookcode, search book in the table, show the book details if found else display "not found" message 
import pymysql
con=pymysql.connect(host="buktult3uitjon7amj7n-mysql.services.clever-cloud.com",
user="umqwpl7tg0xdpbx6",
passwd="53IOY90xH96QLXCyhpcH",
database="buktult3uitjon7amj7n"
)
myCursor=con.cursor()
try:
   bc=int(input('enter bookcode : '))
   myCursor.execute("select bookname,category,publication,edition,price,review from books where bookcode=%d" %bc)
   rec=myCursor.fetchone()
   print('bookname     : %s' %rec[0])
   print('category : %s' %rec[1])
   print('publication : %d' %rec[2])
   print('edition : %d' %rec[3])
   print('price : %d' %rec[4])
   print('review : %s' %rec[5])
   
   if rec:
        print("book available!!!")
   else:
        print("book does not exist")

except:
   print("book not available!!!!")

con.commit()
con.close()