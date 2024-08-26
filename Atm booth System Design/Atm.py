#-----------------------------------------------#
#           WELCOME TO ATM BOOTH                |
#                                               |
#            MD: RASEL SARKER                   |
#-----------------------------------------------#


print("\nWELCOME TO ATM BOOTH")
userpin=99999

currentUser=None

while(True):
    if currentUser==None:
        print("\nNO USER Longin!\n")
        ch=input("Register or Login(R/L):")
        if ch=="R":
            name=input("ACCOUNT NAME:")
            nu=input("ACCOUNT NUMBER:")
            pin=int(input("Enter your 5 digit pin number:"))

            if pin!=userpin:
                print("Invalid pin! please try again\n")

            else:
                option=input("Deposit or Withdraw(d/w):")
                if option=="d":
                    DepositAmount=input("Inter Deposit Amount:")
                    print(DepositAmount, "$Have been deposited into your account:")
                          
                if option=="w":
                    WithdrawAmount=input("Inter Withdraw Amount:")
                    print(WithdrawAmount, "$Have been withdraw into your account:")
            Exit=input("Would you like to continue?(y/n):")

            if Exit=="n":
                print("Thanks for using ATM card\n")
                break
            else:
                continue
            

