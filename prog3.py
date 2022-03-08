# Write a program to take input and add new books to the DB table 
import pymysql
con=pymysql.connect(host="buktult3uitjon7amj7n-mysql.services.clever-cloud.com",
user="umqwpl7tg0xdpbx6",
passwd="53IOY90xH96QLXCyhpcH",
database="buktult3uitjon7amj7n"
)
myCursor=con.cursor()
bc=int(input('enter bookcode: '))
bnm=input('enter bookname: ')
ca=input('enter category: ')
au=input('enter author: ')
pub=int(input('enter publication: '))
edi=int(input('enter edition: '))
pri=int(input('enter price: '))
riv=input("enter review: ")
myCursor.execute("insert into books values(%d,%s,%s,%s,%d,%d,%d,%s)" %(bc,bnm,ca,au,pub,edi,pri,riv))

con.commit()
print("data sucssesfuly store")
myCursor.close()

