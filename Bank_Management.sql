CREATE DATABASE BankManagement;
GO

USE BankManagement;
GO

CREATE TABLE Customers
(
    CustomerID INT IDENTITY(1,1) PRIMARY KEY,
    FullName VARCHAR(100) NOT NULL,
    Phone VARCHAR(15),
    Email VARCHAR(100),
    Address VARCHAR(200),
    CreatedAt DATETIME DEFAULT GETDATE()
);
GO

CREATE TABLE Accounts
(
    AccountNo INT IDENTITY(1001,1) PRIMARY KEY,
    CustomerID INT  NOT NULL,
    AccountType VARCHAR(20) DEFAULT 'Savings',
    Balance DECIMAL(10,2) DEFAULT 0,
    Status VARCHAR(20) DEFAULT 'Active',
    CreatedAt DATETIME DEFAULT GETDATE(),

    FOREIGN KEY (CustomerID)
    REFERENCES Customers(CustomerID)
);
GO

CREATE TABLE Transactions
(
    TransactionID INT IDENTITY(1,1) PRIMARY KEY,
    AccountNo INT NOT NULL,
    TransactionType VARCHAR(20),
    Amount DECIMAL(10,2),
    TransactionDate DATETIME DEFAULT GETDATE(),

    FOREIGN KEY (AccountNo)
    REFERENCES Accounts(AccountNo)
);
GO

select * from Transactions;
select * from Customers;
select * from Transactions;
select * from Accounts;



INSERT INTO Customers (FullName, Phone, Email, Address) VALUES
('Aarav Sharma', '9876543210', 'aarav@gmail.com', 'Delhi'),
('Priya Verma', '9123456789', 'priya@gmail.com', 'Mumbai'),
('Rahul Kumar', '9988776655', 'rahul@gmail.com', 'Patna'),
('Ananya Singh', '9811223344', 'ananya@gmail.com', 'Bangalore'),
('Amit Patel', '9722334455', 'amit@gmail.com', 'Ahmedabad'),
('Neha Gupta', '9633445566', 'neha@gmail.com', 'Kolkata'),
('Rohit Verma', '9544556677', 'rohit@gmail.com', 'Chennai'),
('Pooja Mishra', '9455667788', 'pooja@gmail.com', 'Lucknow'),
('Vikram Malhotra', '9366778899', 'vikram@gmail.com', 'Hyderabad'),
('Sneha Reddy', '9277889900', 'sneha@gmail.com', 'Pune');




INSERT INTO Accounts ( CustomerID, AccountType, Balance, Status) VALUES
(1, 'Savings', 5000.00, 'Active'),
(2, 'Current', 15000.00, 'Active'),
(3,'Savings', 8500.00, 'Active'),
(4, 'Savings', 12000.00, 'Active'),
(5, 'Current', 25000.00, 'Active'),
(6, 'Savings', 3400.00, 'Active'),
(7, 'Savings', 6700.00, 'Active'),
(8,'Current', 18000.00, 'Active'),
(9,'Savings', 9200.00, 'Active'),
(10, 'Savings', 11000.00, 'Active');
