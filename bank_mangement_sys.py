from collections import OrderedDict

accounts = OrderedDict()
next_id = 1

def create_account():
    global next_id

    name = input("Enter Customer Name: ")
    balance = float(input("Enter Initial Balance: "))

    accounts[next_id] = {
        "name": name,
        "balance": balance
    }

    print("Account Created Successfully")
    print("Account Number:", next_id)

    next_id += 1

def show_all_accounts():
    if not accounts:
        print("No Accounts Found")
    else:
        print("====== ALL ACCOUNTS ======")
        for account_id, account in accounts.items():
            print("Account Number:", account_id)
            print("Customer Name:", account["name"])
            print("Balance:", account["balance"])
            print("--------------------------")

def deposit():
    acc_no = input("Enter Account Number: ")
    account = accounts.get(int(acc_no))

    if account:
        amount = float(input("Enter Deposit Amount: "))
        account["balance"] += amount
        print("Deposit Successful")
        print("Updated Balance:", account["balance"])
    else:
        print("Account Not Found")

def withdraw():
    acc_no = input("Enter Account Number: ")
    account = accounts.get(int(acc_no))

    if account:
        amount = float(input("Enter Withdraw Amount: "))

        if amount <= account["balance"]:
            account["balance"] -= amount
            print("Amount Withdrawn Successfully")
            print("Updated Balance:", account["balance"])
        else:
            print("Insufficient Balance")
    else:
        print("Account Not Found")

def check_balance():
    acc_no = input("Enter Account Number: ")
    account = accounts.get(int(acc_no))

    if account:
        print("Account Number:", acc_no)
        print("Customer Name:", account["name"])
        print("Current Balance:", account["balance"])
    else:
        print("Account Not Found")

def delete_account():
    acc_no = input("Enter Account Number: ")
    account = accounts.get(int(acc_no))

    if account:
        del accounts[int(acc_no)]
        print("Account Deleted Successfully")
    else:
        print("Account Not Found")

while True:
    print("\n====== BANK MANAGEMENT SYSTEM ======")
    print("1. Create Account")
    print("2. Show All Accounts")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Check Balance")
    print("6. Delete Account")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        show_all_accounts()
    elif choice == "3":
        deposit()
    elif choice == "4":
        withdraw()
    elif choice == "5":
        check_balance()
    elif choice == "6":
        delete_account()
    elif choice == "7":
        print("Thank You")
        break
    else:
        print("Invalid Choice")