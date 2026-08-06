accounts = {}
next_id = 1
while True:
    print("\n===== BANK MANAGER SYSTEM =====")
    print("1. Create Account")
    print("2. Show All Accounts")
    print("3. Deposit")
    print("4.Withdraw")
    print("5.Check Balance")
    print("6. Exit")
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
            for acc_no in accounts:
                print("Account No :", acc_no)
                print("Name :", accounts[acc_no]["name"])
                print("Balance :", accounts[acc_no]["balance"])
                print()
    elif choice == "3":
        acc_no = int(input("Enter Account Number: "))
        if acc_no in accounts:
            amount = float(input("Enter Deposit Amount: "))
            accounts[acc_no]["balance"] = accounts[acc_no]["balance"] + amount
            print("Amount Deposited Successfully")
            print("Updated Balance:", accounts[acc_no]["balance"])
        else:
            print("Account Not Found")
    elif choice == "4":
        acc_no = int(input("Enter Account Number: "))
        if acc_no in accounts:
            amount = float(input("Enter Withdraw Amount: "))
            if amount <= accounts[acc_no]["balance"]:
                accounts[acc_no]["balance"] = accounts[acc_no]["balance"] - amount
                print("Amount Withdrawn Successfully")
                print("Remaining Balance:", accounts[acc_no]["balance"])
            else:
                print("Insufficient Balance")
        else:
            print("Account Not Found")
    elif choice == "5":
        acc_no = int(input("Enter Account Number: "))

        if acc_no in accounts:
            print("Account Holder :", accounts[acc_no]["name"])
            print("Current Balance:", accounts[acc_no]["balance"])
        else:
            print("Account Not Found")
    elif choice == "6":
        print("Thank You")
        break
    else:
        print("Invalid Choice")