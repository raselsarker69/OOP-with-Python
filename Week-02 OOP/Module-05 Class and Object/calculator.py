class Calculator:
    brand = 'casio'
    
    def add(self, num1, num2):
        deduct = num1 - num2
        multiples = num1 * num2
        devide = num1 // num2
        summation = num1 + num2

        print("Deduct:", deduct)
        print("Multiples:", multiples)
        print("Divide:", devide)
        print("Sum:", summation)


operation = Calculator()
operation.add(10, 2)

#-----------------------------------------------------------

class Calculator:
    Brand = 'Casio'

    def __init__(self, owner, brand, price):

        self.owner = owner
        self.brand = brand
        self.price = price

    def add(self, num1, num2):
        deduct = num1 - num2
        multiples = num1 * num2
        devide = num1 // num2
        summation = num1 + num2

        print("Deduct:", deduct)
        print("Multiples:", multiples)
        print("Divide:", devide)
        print("Sum:", summation)


my_calculator = Calculator('Rasel sarker','Casio',1000)
print(my_calculator.owner,my_calculator.brand,my_calculator.price)
my_calculator.add(10,2)