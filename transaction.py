from database import get_connection

def deposit_money():
    account_no = int(input("Enter Account No: "))
    amount = float(input("Enter Deposit Amount: "))

    if amount <= 0:
        print("\n[ERROR] Invalid amount.")
        return

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT Balance
        FROM Accounts
        WHERE AccountNo = ?
    """, (account_no,))

    account = cursor.fetchone()

    if account is None:
        print("\n[ERROR] Account not found.")
        cursor.close()
        connection.close()
        return

    cursor.execute("""
        UPDATE Accounts
        SET Balance = Balance + ?
        WHERE AccountNo = ?
    """, (amount, account_no))

    cursor.execute("""
        INSERT INTO Transactions
        (AccountNo, TransactionType, Amount)
        VALUES (?, ?, ?)
    """, (account_no, "Deposit", amount))

    connection.commit()
    print(f"\n[SUCCESS] Deposited ₹{amount} to Account No: {account_no}")

    cursor.close()
    connection.close()

def withdraw_money():
    account_no = int(input("Enter Account No: "))
    amount = float(input("Enter Withdrawal Amount: "))

    if amount <= 0:
        print("\n[ERROR] Invalid amount.")
        return

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT Balance
        FROM Accounts
        WHERE AccountNo = ?
    """, (account_no,))

    account = cursor.fetchone()

    if account is None:
        print("\n[ERROR] Account not found.")
        cursor.close()
        connection.close()
        return

    balance = float(account[0])

    if amount > balance:
        print(f"\n[ERROR] Insufficient balance! Current Balance is ₹{balance}")
        cursor.close()
        connection.close()
        return

    cursor.execute("""
        UPDATE Accounts
        SET Balance = Balance - ?
        WHERE AccountNo = ?
    """, (amount, account_no))

    cursor.execute("""
        INSERT INTO Transactions
        (AccountNo, TransactionType, Amount)
        VALUES (?, ?, ?)
    """, (account_no, "Withdraw", amount))

    connection.commit()
    print(f"\n[SUCCESS] Withdrawn ₹{amount} from Account No: {account_no}")

    cursor.close()
    connection.close()

def check_balance():
    account_no = int(input("Enter Account No: "))

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT Balance
        FROM Accounts
        WHERE AccountNo = ?
    """, (account_no,))

    account = cursor.fetchone()

    if account is None:
        print("\n[ERROR] Account not found.")
    else:
        print(f"\nAccount No      : {account_no}")
        print(f"Current Balance : ₹{account[0]}")

    cursor.close()
    connection.close()

def transaction_history():
    account_no = int(input("Enter Account No: "))

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT TransactionID,
               TransactionType,
               Amount,
               TransactionDate
        FROM Transactions
        WHERE AccountNo = ?
        ORDER BY TransactionDate DESC
    """, (account_no,))

    transactions = cursor.fetchall()
    print(f"\n================ TRANSACTION HISTORY (A/C: {account_no}) ================")

    if not transactions:
        print("No transactions found for this account.")
    else:
        for txn in transactions:
            print(f"Txn ID : {txn.TransactionID} | Type: {txn.TransactionType:<10} | Amount: ₹{txn.Amount:<8} | Date: {txn.TransactionDate}")
        print("=" * 70)

    cursor.close()
    connection.close()