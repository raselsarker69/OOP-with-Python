class User:
    users = []

    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.loans_taken = 0
        self.transaction_history = []

    def generate_account(self):
        return len(self.name) + len(self.email)

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"\nDeposit: ${amount}. New Balance: ${self.balance}")
        else:
            print(f"\nInvalid Deposit amount")

    def withdrawal(self, amount):
        if amount > 0:
            self.balance -= amount
            print(f"\nWithdraw: ${amount}. New Balance: ${self.balance}")
        else:
            print(f"\nInvalid withdrawal amount")

    def check_balance(self):
        return self.balance

    def take_loan(self, amount):
        if self.loans_taken < 2:
            self.balance += amount
            self.loans_taken += 1
            self.transaction_history.append(f'Loan Taken: ${amount}')
        else:
            return "Maximum number of loans reached."

    def transfer_amount(self, to_account, amount):
        if to_account in User.users:
            if self.balance >= amount:
                self.balance -= amount
                to_account.deposit(amount)
                self.transaction_history.append(f'Transfer to {to_account.name}: ${amount}')
            else:
                return "Sorry, your account does not have sufficient balance."
        else:
            return "Account does not exist."

    def check_transaction_history(self):
        return self.transaction_history

class SavingsAccount(User):
    def __init__(self, name, email, address, interest_rate):
        super().__init__(name, email, address, "SavingsAccount")
        self.interest_rate = interest_rate

    def interest(self):
        interest = self.balance * (self.interest_rate / 100)
        print("\n--Applied interest!\n")
        self.deposit(interest)

class CurrentAccount(User):
    def __init__(self, name, email, address, limit):
        super().__init__(name, email, address, "CurrentAccount")
        self.limit = limit

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            print(f"\nWithdraw: ${amount}. New Balance: ${self.balance}")
        else:
            print(f"\nInvalid withdraw amount")

class Admin:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def delete_user_account(self, user):
        if user in User.users:
            User.users.remove(user)
        else:
            return "User not found."

    def user_account_list(self):
        return [user.name for user in User.users]

    def total_available_balance(self):
        total_balance = sum(user.balance for user in User.users)
        return f'Total Available Balance: ${total_balance}'

    def total_loan_amount(self):
        return sum(user.balance for user in User.users if user.loans_taken > 0)

# Main program

currentUser = None
adminUser = None

while True:
    if adminUser is None and currentUser is None:
        print("\nNo Admin and User Logged In!\n")
        ch = input("Register or Login (R/L):")
        if ch == "R":
            option = input("Admin or User (A/U):")
            if option == "A":
                name = input("Admin Name:")
                email = input("Enter Email Address:")
                adminUser = Admin(name, email)
                print("Welcome, Admin!")
                print("1. Delete User Account")
                print("2. Show All User Account List:")
                print("3. Generate_account")
                print("4. Total Avilable Balance:")
                print("5. Total Loan Amount")
                print("6. Loan OFF or ON")
                print("7. Logout\n")

                op=int(input("Enter option:"))

                if op==1:
                    User=input("Enter User Account:")
                    Admin.Delete_user_account(User)
            
                elif op==2:
                    Admin.user_account_list()

                elif op==3:
                    Admin.Total_available_balance()

                elif op==4:
                    Admin.Total_loan_amount()

                elif op==5:
                    Admin.Loan_off_or_on()

                elif op==6:
                    Admin==None
                else:
                    print("\n Invalid option! Please Try Again")

            elif option == "U":
                name = input("User Name:")
                email = input("Enter Email Address:")
                address = input("Enter Address:")
                account_type = input("Savings Account or Current Account (sv/cr):")
                if account_type == "sv":
                    interest_rate = int(input("Interest Rate:"))
                    currentUser = SavingsAccount(name, email, address, interest_rate)
                elif account_type == "cr":
                    limit = int(input("Draft Limit:"))
                    currentUser = CurrentAccount(name, email, address, limit)
                print(f"Welcome, {currentUser.name}!")

        else:
            account_number = input("Account Number:")
            for user in User.users:
                if user.account_number == account_number:
                    currentUser = user
                    print(f"Welcome, {currentUser.name}!")
                    break

    else:
        if isinstance(currentUser, SavingsAccount):
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Generate Account")
            print("4. Check Balance")
            print("5. Take Loan")
            print("6. Transfer Amount")
            print("7. Check Transaction History")
            print("8. Logout")

            ch = input("Choose an option:")

            if ch == 1:
                amount = int(input("Deposit amount:"))
                currentUser.deposit(amount)

            elif ch == 2:
                amount = int(input("Withdraw amount:"))
                currentUser.withdraw(amount)

            elif ch == 3:
                print(f"Generated Account: {currentUser.generate_account()}")

            elif ch == 4:
                print(f"Current Balance: ${currentUser.check_balance()}")

            elif ch == 5:
                amount = int(input("Loan Amount:"))
                currentUser.take_loan(amount)

            elif ch == 6:
                to_account = input("Enter the account number to transfer to:")
                amount = int(input("Enter the amount to transfer:"))
                currentUser.transfer_amount(to_account, amount)

            elif ch == 7:
                history = currentUser.check_transaction_history()
                for item in history:
                    print(item)

            elif ch == 8:
                currentUser = None

        elif isinstance(currentUser, CurrentAccount):
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Generate Account")
            print("4. Check Balance")
            print("5. Take Loan")
            print("6. Transfer Amount")
            print("7. Check Transaction History")
            print("8. Logout")

            ch = input("Choose an option:")

            if ch == 1:
                amount = int(input("Deposit amount:"))
                currentUser.deposit(amount)

            elif ch == 2:
                amount = int(input("Withdraw amount:"))
                currentUser.withdraw(amount)

            elif ch == 3:
                print(f"Generated account with ID: {currentUser.generate_account()}")

            elif ch == 4:
                print(f"Current Balance: ${currentUser.check_balance()}")

            elif ch == 5:
                amount = int(input("Loan amount:"))
                currentUser.take_loan(amount)

            elif ch == 6:
                to_account = input("Enter the account number to transfer to:")
                amount = int(input("Enter the amount to transfer:"))
                currentUser.transfer_amount(to_account, amount)

            elif ch == 7:
                history = currentUser.check_transaction_history()
                for item in history:
                    print(item)

            elif ch == 8:
                currentUser=None
            else:
                print("\n Invalid option! Please Try Again")