from abc import ABC,abstractmethod

class Account(ABC):
    accounts=[] # Ai account ar list a sob account ar property acay.
     
    def __init__(self,name,ac_number,password,type) -> None:
        self.name=name
        self.ac_number=ac_number
        self.password=password
        self.type=type
        self.balance=0
        Account.account.append(self)

    def deposit(self,amount):
        if amount>=0:
            self.balance+=amount
        else:
            print(f'\nInvalid account\n')

    def withdraw(self,amount):
        if amount>=0 and amount<=self.balance:
            self.balance-=amount
        else:
            print(f'\nInvalid account\n')


    def changeinfo(self,name):
        self.name=name


    # polimorfujom ar over loading idea
    # over loading of method change info
    def changeinfo(self,name,password):
        self.name=name
        self.password=password

    @abstractmethod
    def show_info(self):
        pass

class SavingsAccount:
    def __init__(self,name,ac_number,password,interestRate) -> None:
        super().__init__(name,ac_number,password,interestRate,"savings")
        self.irate=interestRate
    
    # parent ar kacay abstract method thaklay setha implement kortay hoy
    def show_info(self):
        print(f"\n Infos of account: {self.name}\n")
        print(f"\n Account Number: {self.acc_no}\n")
        print(f"\n Account Type: {self.Type}\n")
        print(f"\n Balance: {self.balance}\n")
        
    def applyinterest(self):
        interest=self.balance*(self.iRate/100)
        print(f"\n Applied interest:{interest}")
        self.deposit(interest)

class SpecialAccount(Account):
    def __init__(self,name,ac_number,password,limit) -> None:
        super().__init__(name,ac_number,password,"speacil")
        self.limit=limit

    # over rides the method inside 
    def withdraw(self,amount):
        if amount>=0 and amount<=self.limit:
            self.balance-=amount
        else:
            print(f'\nInvalid account\n')

    #parent ar kacay abstract methods thaklay setha implement kortay hoy 
    def show_info(self):
        print(f"\n Infos of :{self.Type}, account: {self.name}\n")
        print(f"\n Account Number: {self.acc_no}\n")
        print(f"\n Balance: {self.balance}\n")

# user track rakar jonno akta current user niboo
currentUser=None

while(True):
    if currentUser==None:
        print(f"\n No user login!:")
        ch=input("\n Register/Login (R/L):")

        if ch=="R":
            name=input("User name:")
            no=input("Account Number:")
            pas=input("Password:")
            a=input("\n Savings Account or Speacial Account(sv/sp):")

            if a=="sv":
                iRate=input("Interest Rate:")
                currentUser=SavigsAccount(name,no,pas,iRate)
            
            elif a=="sp":
                lim=input("Draf limit:")
                currentUser=SpeacilAccount(name,no,pas,lim)

        else:
           no=input("Account Number:")
           for account in Account.accounts:
               if account.account_no==no:
                   currentUser=account
                   break
               
    else:
        print(f"\n WELLCOME :{currentUser.name}!\n")
        if currentUser.type=="SavigsAccount":

            print("1.withdraw")
            print("2.Deposit")
            print("3.showinfo")
            print("4.Changeinfo")
            print("5.Applyinterest")
            print("6.Logout\n")

            op=int(input("Choice option:"))

            if op==1:
                amount=int(input("Enter withdraw amount:"))
                currentUser.withdraw(amount)

            elif op==2:
                amount=int(input("Deposit amount:"))
                currentUser.deposit(amount)
            
            elif op==3:
                currentUser.showinfo()

            elif op==4:
                currentUser.changeinfo()

            elif op==5:
                currentUser.Applyinterest()

            elif op==6:
                currentUser==None
            else:
                print("\n Invalid option")

        else:

            print("1.withdraw")
            print("2.Deposit")
            print("3.showinfo")
            print("4.Changeinfo")
            print("5.Logout\n")

            op=int(input("Choice option:"))

            if op==1:
                amount=int(input("Enter withdraw amount:"))
                currentUser.withdraw(amount)

            elif op==2:
                amount=int(input("Deposit amount:"))
                currentUser.deposit(amount)
            
            elif op==3:
                currentUser.showinfo()

            elif op==4:
                currentUser.changeinfo()

            elif op==5:
                currentUser.Applyinterest()

            elif op==6:
                currentUser==None
            else:
                print("\n Invalid option")

        


            