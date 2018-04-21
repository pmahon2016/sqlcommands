import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\inetpub\wwwroot\BDC\HSD\HSD.accdb;')
cursor = conn.cursor()
#sample table
#cursor.execute('create table CUSTOMER3 (EmailAddress varchar(255) NOT NULL,LastName varchar(45),FirstName varchar(45), Phone varchar(45),StreetAddress varchar(255),City varchar(45),State varchar(15),Zip varchar(15),PRIMARY KEY(EmailAddress) );')

#Auto table and fields
#cursor.execute('CREATE TABLE AUTO (AutoCapacity varchar(100), AutoColor varchar(50), AutoCylinders number, AutoListPrice currency, AutoMake varchar (50), AutoMilageAtDelivery number, AutoModel varchar(50), AutoOptions varchar(255), AutoRegistrationNumber varchar(100), AutoStyle varchar(50), AutoWeight varchar(100), AutoYear varchar(50),  DateofDelivery varchar (50), DateofManufacture varchar(50),  DealershipName varchar(100), NumOfDoors number, OdometerReading number, VehicleIDNum number NOT NULL, PlaceOfManufacture varchar(100), PRIMARY KEY (VehicleIDNum));' )

#Customer
#cursor.execute('CREATE TABLE CUSTOMER (CustomerStreet varchar(150), CustomerIncome currency, CustomerCity varchar(50), CustomerEmailAddress varchar(200), CustomerEmployer varchar (100), CustomerFinancing varchar(50), CustomerGender  varchar(50), CustomerInsurance varchar(255), CustomerBuyLease varchar(100), CustomerlicNum varchar(100), CustomerName varchar(150), CustomerPhone number, CustomerReferOut varchar (50), CustomerRef varchar(50),  RetBuyer varchar(50), TradeIn varchar(50), CustomerZip number, CustomerVehicle varchar(100), CustSS number, OptionalAge number, OptionalRace varchar(50), ExtendedWarranty varchar(50), OfferedTestDrive varchar(50) );' )

#dealership
#cursor.execute('CREATE TABLE DEALER (DealerName varchar(100),DealerInventory number, DealerNumber number, DealerState varchar(50), DealerCity varchar(50), DealerAnnualSales currency);' )

#SalesPerson
#cursor.execute('CREATE TABLE SALESPERSON (SalesYear varchar(25), SalesMonth varchar(25), SalesNumber autoincrement primary key , Name varchar(100), AnnualSalestoDate currency, MonthlySales currency, NumLeasesSold number, PurchaseSold number );' )





conn.commit()

