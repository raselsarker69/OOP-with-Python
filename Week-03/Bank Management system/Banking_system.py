from abc import ABC,abstractmethod
class Account:
    accounts=[] # ai accoount a sob gulo account ar property thakbay
    def __init__(self,name,account_no,password,type) -> None:
        self.name=name
        self.account_no=account_no
        self.password=password
        self.type=type
        self.balance=0

        Account.accounts.append(self)

   
    def deposit(self,amount):
        if amount>=0:
            self.balance+=amount
            print(f"\n Deposit:${amount}.New Balance:${self.balance}")
        else:
            print(f"\n Invalid Deposit amount")

    def withdraw(self,amount):
        if amount>=0:
            self.balance-=amount
            print(f"\n withdraw:${amount}.New Balance:${self.balance}")
        else:
            print(f"\n Invalid withdraw amount")

    # polymorfujom ar over loding methods
    def changeinfo(self,name):
        self.name=name
        print(f"\n change account number:{self.account_no}")

    def changeinfo(self,name,password):
        self.name=name
        self.password=password
        print(f"\n change account number:{self.account_no}")

    @abstractmethod
    def showinfo(self):
        pass

class SavigsAccount(Account):
    def __init__(self, name, account_no, password, interestRate) -> None:
        super().__init__(name, account_no, password, "SavigsAccount")
        self.interestRate=interestRate

    def Applyinterest(self):
        interest=self.balance*(self.interestRate/100)
        print("\n --Applied interest!\n")
        self.deposit(interest)

    def showinfo(self):
        print(f"\n Infos of:{self.type}.Type of:{self.name}")
        print(f"\n Account type:{self.type}")
        print(f"\n Account Name:{self.name}")
        print(f"\n Accouont number:{self.account_no}")
        print(f"\n Current Balanae:{self.balance}")

class SpeacilAccount(Account):
    def __init__(self, name, account_no, password, Limit) -> None:
        super().__init__(name, account_no, password, "SpeacilAccount")
        self.Limit=Limit

    def withdraw(self,amount):
        if amount > 0 and (self.balance - amount) >= -self.limit:
            self.balance-=amount
            print(f"\n withdraw:${amount}.New Balance:${self.balance}")
        else:
            print(f"\n Invalid withdraw amount")

    def showinfo(self):
        print(f"\n Infos of:{self.type}.Type of:{self.name}")
        print(f"\n Account type:{self.type}")
        print(f"\n Account Name:{self.name}")
        print(f"\n Accouont number:{self.account_no}")
        print(f"\n Current Balanae:{self.balance}")

# main program
    
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





        