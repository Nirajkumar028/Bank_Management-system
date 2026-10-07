from database import get_connection

def create_customer():
    name = input("Enter Customer Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO Customers
        (FullName, Phone, Email, Address)
        VALUES (?, ?, ?, ?)
    """, (name, phone, email, address))

    connection.commit()
    print(f"\n[SUCCESS] Customer '{name}' created successfully!")

    cursor.close()
    connection.close()

def view_customers():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT CustomerID, FullName, Phone, Email, Address
        FROM Customers
    """)

    customers = cursor.fetchall()
    print("\n==================== CUSTOMER LIST ====================")

    for customer in customers:
        print(f"Customer ID : {customer.CustomerID}")
        print(f"Name        : {customer.FullName}")
        print(f"Phone       : {customer.Phone}")
        print(f"Email       : {customer.Email}")
        print(f"Address     : {customer.Address}")
        print("-" * 55)

    cursor.close()
    connection.close()