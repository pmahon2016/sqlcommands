

import MySQLdb

db = MySQLdb.connect('localhost','root', 'password', 'test')

cursor = db.cursor()


cursor.execute("select * from Salesperson")

myresults = cursor.fetchall()

for i in myresults:
    print(i)
