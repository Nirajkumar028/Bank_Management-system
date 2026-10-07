from customer import create_customer, view_customers
from account import create_account, view_accounts
from transaction import (
    deposit_money,
    withdraw_money,
    check_balance,
    transaction_history
)

def main():
    while True:
        print("\n==============================")
        print("     BANK MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Create Customer")
        print("2. View Customers")
        print("3. Create Account")
        print("4. View Accounts")
        print("5. Deposit Money")
        print("6. Withdraw Money")
        print("7. Check Balance")
        print("8. Transaction History")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_customer()
        elif choice == "2":
            view_customers()
        elif choice == "3":
            create_account()
        elif choice == "4":
            view_accounts()
        elif choice == "5":
            deposit_money()
        elif choice == "6":
            withdraw_money()
        elif choice == "7":
            check_balance()
        elif choice == "8":
            transaction_history()
        elif choice == "9":
            print("Thank you for using Bank Management System!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()