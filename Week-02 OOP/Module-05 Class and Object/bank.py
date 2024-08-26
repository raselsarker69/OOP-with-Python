

class bank:

    def __init__(self,balance):
        self.balance = balance

        self.min_withdrow = 100
        self.max_withdrow = 100000
    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount
        
    def withdrow(self,amount):
        if amount<self.min_withdrow:
            print( f'fokira. you can withdrow below{self.min_withdrow}')  
        if amount>self.max_withdrow: 
            print(f'bank fokir hoya jabay vai{self.max_withdrow}')
        else:
            self.balance -= amount
            print(f' here is your money{amount}')   
            print(f' your balance after withdraw{self.get_balance()}')   
        
brac =bank(1000000)
bank.withdrow(5000)
bank.withdrow(30000)
bank.withdrow(2500)

DBBL =bank(1000000)
bank.deposit(50000)
bank.deposit(100000)
print(DBBL.get_balance())