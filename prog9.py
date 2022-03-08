# Write a program to accept author and publication, display list of books of the author-publication combination 
import pymysql
con=pymysql.connect(host="buktult3uitjon7amj7n-mysql.services.clever-cloud.com",
user="umqwpl7tg0xdpbx6",
passwd="53IOY90xH96QLXCyhpcH",
database="buktult3uitjon7amj7n"
)
myCursor=con.cursor()

au=input("enter auther : ")
pub=int(input('enter publication : '))
myCursor.execute("select auther,publication from books")


rec=myCursor.fetchall()
con.commit()

try:
    print('author     : %s' %rec[0])
    print('publication : %d' %rec[1])
    if rec:
        print("d")
    else:
        print("n")    
   
  
except:
    print("book does not exist!!!!")

con.close()