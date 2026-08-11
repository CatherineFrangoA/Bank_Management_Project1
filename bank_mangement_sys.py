from collections import OrderedDict
accounts = OrderedDict()
next_id = 1
while True:
    print("\n===== BANK MANAGER SYSTEM =====")
    print("1. Create Account")
    print("2. Show All Accounts")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Check Balance")
    print("6. Delete Account")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter Customer Name: ")
        balance = float(input("Enter Initial Balance: "))
        accounts[next_id] = {
            "name": name,
            "balance": balance
        }
        print("Account Created Successfully")
        print("Account Number:", next_id)
        next_id = next_id + 1
    elif choice == "2":
        if len(accounts) == 0:
            print("No Accounts Found")
        else:
            print("\nAccount Details")
            for acc_no, account in accounts.items():
                print("Account No :", acc_no)
                print("Name :", account["name"])
                print("Balance :", account["balance"])
                print()
    elif choice == "3":
        acc_no = int(input("Enter Account Number: "))
        account = accounts.get(acc_no)
        if account:
            amount = float(input("Enter Deposit Amount: "))
            account["balance"] = account["balance"] + amount
            print("Amount Deposited Successfully")
            print("Updated Balance:", account["balance"])
        else:
            print("Account Not Found")
    elif choice == "4":
        acc_no = int(input("Enter Account Number: "))
        account = accounts.get(acc_no)
        if account:
            amount = float(input("Enter Withdraw Amount: "))
            if amount <= account["balance"]:
                account["balance"] = account["balance"] - amount
                print("Amount Withdrawn Successfully")
                print("Updated Balance:", account["balance"])
            else:
                print("Insufficient Balance")
        else:
            print("Account Not Found")
    elif choice == "5":
        acc_no = int(input("Enter Account Number: "))
        account = accounts.get(acc_no)
        if account:
            print("Account Number:", acc_no)
            print("Customer Name:", account["name"])
            print("Current Balance:", account["balance"])
        else:
            print("Account Not Found")
    elif choice == "6":
        acc_no = int(input("Enter Account Number: "))
        account = accounts.get(acc_no)
        if account:
            del accounts[acc_no]
            print("Account Deleted Successfully")
        else:
            print("Account Not Found")
    elif choice == "7":
        print("Thank You")
        break
    else:
        print("Invalid Choice")