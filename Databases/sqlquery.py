import MySQLdb

db = MySQLdb.connect('localhost','root', 'password')

cursor = db.cursor()

cursor.execute("Create Database Test")


