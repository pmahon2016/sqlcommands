import MySQLdb

db = MySQLdb.connect('localhost','pace', 'pace123', 'BMC')

cursor = db.cursor()


cursor.execute('Select version()')


data = cursor.fetchone()

print(data)
