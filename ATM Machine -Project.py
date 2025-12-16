import datetime
print("Welcome to ATM Machine")
password = 1445
attempts = 0
max_attempts = 3
balance = 1000
while attempts < max_attempts:
    pin = int(input("Enter your 4-digit PIN: "))
    if pin == password:
        print("Access Granted")
        print("\nSelect an option:")     
        print("1. Check Balance")     
        print("2. Deposit Money")     
        print("3. Withdraw Money")     
        print("4. Mini Statement")     
        print("5. Exit")
        choice = int(input("Enter choice (1/2/3/4/5): "))
        if choice == 1:
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Current Balance: Rs {balance}")
            print(f"Time: {time}")

        elif choice == 2:
            deposit = int(input("Enter amount to deposit: "))
            balance += deposit
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Deposit successful! New Balance: Rs {balance}")
            print(f"Time: {time}")

        elif choice == 3:
            withdraw = int(input("Enter amount to withdraw: "))
            if withdraw <= balance:
                balance -= withdraw
                time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"Withdrawal successful! Remaining Balance: Rs {balance}")
                print(f"Time: {time}")
            else:
                print("Insufficient funds")

        elif choice == 4:
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Available Balance: Rs {balance}")
            print(f"Time: {time}")

        elif choice == 5:
            print("Thank you for using ATM Machine")

        else:
            print("Invalid option")

        break   
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print(f"Incorrect PIN! Attempts left: {remaining}")
        if remaining == 0:
            print("Account blocked. Please try again later.")
