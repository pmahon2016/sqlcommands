import MySQLdb

db = MySQLdb.connect('localhost','pace', 'pace123', 'BMC')

cursor = db.cursor()


sqltbl = """

CREATE TABLE AUTOINVENTORY (
        VehicleIDNum varchar(50), 
        AutoCapacity integer, 
        AutoColor varchar(50), 
        AutoCylinders integer, 
        AutoFinancedBy varchar(50), 
        AutoListPrice int, 
        AutoMake varchar(50), 
        AutoMilageAtDelivery integer, 
        AutoModel varchar(50), 
        AutoOptions varchar(150), 
        AutoRegistrationInt integer, 
        AutoSalePrice integer, 
        AutoStyle varchar(50), 
        AutoWeight varchar(50), 
        AutoYear varchar(50), 
        DateofDelivery varchar(50), 
        DateofManufacture varchar(50), 
        DateOfSale varchar(50), 
        DealershipName varchar(50), 
        NumOfDoors integer, 
        OdometerReading integer, 
        PlaceOfManufacture varchar(100),
        PRIMARY KEY (VehicleIDNum)
        
    );


CREATE TABLE SALESPERSON (
            SalesID int,
            SalesPersonFName varchar(50),
            SalesPersonLName varchar(50), 
            SalesPersonPhone char(10),
            SalesPersonEmailAddress varchar(50),
            SalesSpeciality varchar(50), 
            Availability varchar(50),
            SalesPersonMonthlyDraw decimal,
            TaxInt int,
            CONSTRAINT SalesID_PK PRIMARY KEY (SalesID)
            );





CREATE TABLE CUSTOMER (

        CustID integer,
        CustFName varchar(20),
        CustLName varchar(20), 
        CustStreet varchar(20), 
        CustCity varchar(20), 
        CustZip int,
        CustAnnnualIncome decimal, 
        CustomerEmail varchar(20), 
        CustomerEmployer varchar(20),
        CustomerFinancing varchar(20),
        CustGender varchar(20),
        CustomerInsuranceNum varchar(20),
        CustomerLeaseBuy varchar(20), 
        CustomerLicenseNum varchar(20),  
        CustomerPhone Char(10), 
        CustomerReferOut varchar(20),
        CustomerReturnBuyer varchar(120), 
        CustomerSocial int, 
        CustomerTradeIn varchar(20),  
        HowCustomerFoundDealership varchar(20), 
        OfferedTestDrive varchar(20), 
        RentOwnCustomerHome varchar(20), 
        ExtendedWarranty varchar(20),        
        PRIMARY KEY (CustID)
                
    );




CREATE TABLE DEALERSHIP (
        DealershipName varchar(50) PRIMARY KEY, 
        Owner varchar(50),   
        DealerFinancing varchar(50), 
        LicenseNum int,
        AutoMake varchar(50), 
        NumModels varchar(50),
        DealershipStreet varchar(50),
        DealershipCity varchar(50),
        DealershipState varchar(20),
        DealershipZip int
        
        );



CREATE TABLE BILLOFSALE (
        BOSNum int NOT NULL auto_increment,
        VehicleIDNum char(50), 
        SalesID int,
        AutoCapacity int, 
        AutoColor varchar(50), 
        AutoCylinders int, 
        AutoMake varchar(50), 
        AutoModel varchar(50), 
        AutoRegistrationInt int, 
        AutoSalePrice  decimal, 
        AutoStyle varchar(50), 
        AutoYear varchar(50), 
        CustID integer,
        CustomerAddress varchar(100), 
        CustomerCity varchar(50), 
        CustomerFinancing varchar(50), 
        CustomerLeaseBuy varchar(50), 
        DateOfSale varchar(50), 
        Dealer varchar(50) , 
        NumOfDoors int, 
        OdometerReading int, 
        SalesPriceMinusSticker varchar(50), 
        ExtendedWarranty varchar(50),
        CONSTRAINT BOSNum_PK PRIMARY KEY(BOSNum),
CONSTRAINT VehicleID_FK FOREIGN KEY (VehicleIDNum) REFERENCES AUTOINVENTORY(VehicleIDNum),
        CONSTRAINT Sales_FK  FOREIGN KEY (SalesID) REFERENCES SALESPERSON(SalesID),
        CONSTRAINT CustID_FK FOREIGN KEY (CustID) REFERENCES CUSTOMER(CustID),
        CONSTRAINT Dealer_FK FOREIGN KEY (Dealer) REFERENCES Dealership(DealershipName)
       
    );


CREATE TABLE WARRANTY (
        VehicleID char(50),
        CustID int, 
        DealershipName varchar(50) PRIMARY KEY, 
        Owner varchar(50),   
        DealerFinancing varchar(50), 
        LicenseNum int,
        AutoMake varchar(50), 
        NumModels varchar(50),
        DealershipStreet varchar(50),
        DealershipCity varchar(50),
        DealershipState varchar(20),
        DealershipZip int



"""




cursor.execute(sqltbl)




