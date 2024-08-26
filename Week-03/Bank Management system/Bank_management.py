class User:
    users = []
    loan_enabled = True
 
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = len(User.users) + 1
        self.balance = 0
        self.loans_taken = 0
        self.transaction_history = []
 
    def generate_account(self):
        return len(self.name) + len(self.email)
 
    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: ${amount}")
            print(f"\nDeposit: ${amount}. New Balance: ${self.balance}")
        else:
            print("\nInvalid deposit amount")
 
    def withdrawal(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transaction_history.append(f"Withdraw: ${amount}")
                print(f"\nWithdraw: ${amount}. New Balance: ${self.balance}")
            else:
                print("\nWithdrawal amount exceeded.")
        else:
            print("\nInvalid withdrawal amount")
 
    def check_balance(self):
        return self.balance
 
    def take_loan(self, amount):
        if self.loans_taken < 2:
            if User.loan_enabled:
                self.balance += amount
                self.loans_taken += 1
                self.transaction_history.append(f'Loan Taken: ${amount}')
                print(f"\nLoan taken: ${amount}. New Balance: ${self.balance}")
            else:
                print("\nLoans are currently disabled by the bank.")
        else:
            print("\nMaximum number of loans reached.")
 
    def transfer_amount(self, to_account, amount):
        to_user = None
        for user in User.users:
            if user.name == to_account:
                to_user = user
                break
 
        if to_user:
            if self.balance >= amount:
                self.balance -= amount
                to_user.deposit(amount)
                self.transaction_history.append(f'Transfer to {to_account}: ${amount}')
                print(f"\n${amount} transferred to {to_account}. New Balance: ${self.balance}")
            else:
                print("\nSorry, your account does not have sufficient balance.")
        else:
            print("\nAccount does not exist.")
 
    def check_transaction_history(self):
        return self.transaction_history
 
 
class SavingsAccount(User):
    def __init__(self, name, email, address, interest_rate):
        super().__init__(name, email, address, "SavingsAccount")
        self.interest_rate = interest_rate
 
    def interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.deposit(interest)
        self.transaction_history.append(f'Interest Applied: ${interest}')
 
 
class CurrentAccount(User):
    def __init__(self, name, email, address, overdraft_limit):
        super().__init__(name, email, address, "CurrentAccount")
        self.overdraft_limit = overdraft_limit
 
    def withdrawal(self, amount):
        if amount > 0:
            if self.balance + self.overdraft_limit >= amount:
                self.balance -= amount
                self.transaction_history.append(f'Withdraw: ${amount}')
                print(f"\nWithdraw: ${amount}. New Balance: ${self.balance}")
            else:
                print("\nWithdrawal amount exceeded.")
        else:
            print("\nInvalid withdrawal amount")
 
 
class Admin:
    def __init__(self, name, email):
        self.name = name
        self.email = email
 
    def delete_user_account(self, username):
        for user in User.users:
            if user.name == username:
                User.users.remove(user)
                print(f"Account of {username} deleted.")
                return
        print("User not found.")
 
    def user_account_list(self):
        print("\nList of User Accounts:")
        for user in User.users:
            print(f"Name: {user.name}, Email: {user.email}")
 
    def total_available_balance(self):
        total_balance = sum(user.balance for user in User.users)
        print(f"Total Available Balance: ${total_balance}")
 
    def total_loan_amount(self):
        total_loan = sum(user.check_balance() for user in User.users if user.loans_taken > 0)
        print(f"Total Loan Amount: ${total_loan}")
 
    def loan_off_or_on(self, enable):
        User.loan_enabled = enable
        status = "enabled" if enable else "disabled"
        print(f"Loan feature is {status}.")
 
 
# Main program
currentUser = None
adminUser = None
 
while True:
    if adminUser is None and currentUser is None:
        print("\nNo Admin and User Logged In!\n")
        choice = input("Register or Login (R/L):")
        if choice == "R":
            option = input("Admin or User (A/U):")
            if option == "A":
                name = input("Admin Name:")
                email = input("Enter Email Address:")
                adminUser = Admin(name, email)
                print("Welcome, Admin!")
 
            elif option == "U":
                name = input("User Name:")
                email = input("Enter Email Address:")
                address = input("Enter Address:")
                account_type = input("Savings Account or Current Account (S/C):")
                if account_type == "S":
                    interest_rate = float(input("Interest Rate (%):"))
                    currentUser = SavingsAccount(name, email, address, interest_rate)
                elif account_type == "C":
                    overdraft_limit = float(input("Overdraft Limit:"))
                    currentUser = CurrentAccount(name, email, address, overdraft_limit)
                User.users.append(currentUser)
                print(f"Welcome, {currentUser.name}!")
 
            else:
                print("Invalid option. Please Try Again.")
 
        else:
            username = input("Enter your username:")
            for user in User.users:
                if user.name == username:
                    currentUser = user
                    print(f"Welcome, {currentUser.name}!")
                    break
    else:
        if isinstance(currentUser, SavingsAccount) or isinstance(currentUser, CurrentAccount):
            # User interactions
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Take Loan")
            print("5. Transfer Amount")
            print("6. Check Transaction History")
            print("7. Logout")
 
            choice = int(input("Choose an option:"))
 
            if choice == 1:
                amount = float(input("Deposit amount:"))
                currentUser.deposit(amount)
 
            elif choice == 2:
                amount = float(input("Withdraw amount:"))
                currentUser.withdrawal(amount)
 
            elif choice == 3:
                print(f"Current Balance: ${currentUser.check_balance()}")
 
            elif choice == 4:
                amount = float(input("Loan Amount:"))
                currentUser.take_loan(amount)
 
            elif choice == 5:
                to_account = input("Enter the recipient's username:")
                amount = float(input("Enter the amount to transfer:"))
                currentUser.transfer_amount(to_account, amount)
 
            elif choice == 6:
                history = currentUser.check_transaction_history()
                print("\nTransaction History:")
                for item in history:
                    print(item)
 
            elif choice == 7:
                currentUser = None
 
            else:
                print("Invalid option. Please Try Again.")
 
        elif isinstance(adminUser, Admin):
            # Admin interactions
            print("1. Delete User Account")
            print("2. Show All User Account List")
            print("3. Total Available Balance")
            print("4. Total Loan Amount")
            print("5. Loan OFF or ON")
            print("6. Logout")
 
            admin_choice = int(input("Choose an option:"))
 
            if admin_choice == 1:
                user_to_delete = input("Enter the username to delete:")
                adminUser.delete_user_account(user_to_delete)
 
            elif admin_choice == 2:
                adminUser.user_account_list()
 
            elif admin_choice == 3:
                adminUser.total_available_balance()
 
            elif admin_choice == 4:
                adminUser.total_loan_amount()
 
            elif admin_choice == 5:
                enable_loan = input("Enable or Disable loan feature (ON/OFF):")
                if enable_loan == "ON":
                    adminUser.loan_off_or_on(True)
                elif enable_loan == "OFF":
                    adminUser.loan_off_or_on(False)
 
            elif admin_choice == 6:
                adminUser = None
 
            else:
                print("Invalid option. Please Try Again.")