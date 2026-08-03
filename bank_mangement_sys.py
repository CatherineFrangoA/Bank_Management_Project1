accounts = {}
next_id = 1

while True:
    print("\n===== BANK MANAGER SYSTEM =====")
    print("1. Create Account")
    print("2. Show All Accounts")
    print("3. Exit")

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
        print("Thank You")
        break

    else:
        print("Invalid Choice")