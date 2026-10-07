from database import get_connection

def create_account():
    customer_id = int(input("Enter Customer ID: "))
    account_type = input("Enter Account Type (Savings/Current): ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT CustomerID
        FROM Customers
        WHERE CustomerID = ?
    """, (customer_id,))

    customer = cursor.fetchone()

    if customer is None:
        print("\n[ERROR] Customer not found.")
        cursor.close()
        connection.close()
        return

    cursor.execute("""
        INSERT INTO Accounts
        (CustomerID, AccountType, Balance)
        VALUES (?, ?, ?)
    """, (customer_id, account_type, 0))

    connection.commit()
    print(f"\n[SUCCESS] {account_type} Account created successfully for Customer ID: {customer_id}!")

    cursor.close()
    connection.close()

def view_accounts():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT AccountNo, CustomerID, AccountType, Balance, Status
        FROM Accounts
    """)

    accounts = cursor.fetchall()
    print("\n===================== ACCOUNT LIST =====================")

    for account in accounts:
        print(f"Account No  : {account.AccountNo}")
        print(f"Customer ID : {account.CustomerID}")
        print(f"Type        : {account.AccountType}")
        print(f"Balance     : ₹{account.Balance}")
        print(f"Status      : {account.Status}")
        print("-" * 55)

    cursor.close()
    connection.close()