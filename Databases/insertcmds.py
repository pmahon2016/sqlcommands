
import MySQLdb

db = MySQLdb.connect('localhost','root', 'password', 'test')

cursor = db.cursor()





sqltbl = """


INSERT into SALESPERSON (SalesID, SalesPersonFName,SalesPersonLName, SalesPersonPhone, 
SalesPersonEmailAddress,  SalesSpeciality, Availability,SalesPersonMonthlyDraw, TaxInt) 

Values ( 006, 'John', 'Smith',8323489122, 'jsmith@besla.com', 'Sports' , 'TWTFSat',2000, 873377744 ); 


"""
cursor.execute(sqltbl)

db.commit()


