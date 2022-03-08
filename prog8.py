# Write a program to accept bookcode, display the book data and ask "Do you want to delete?" if "yes" delete the book from the table 
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
   
  data=input('Do you want to Delete? (yes/no): ')
  myCursor.execute("delete from books where bookcode=%d" %bc)

  if data=="yes":
    print("data deleted sucssesfuly!!!")
  else:
    print("exit")    

except:
    print("exit")

con.commit()
con.close()

