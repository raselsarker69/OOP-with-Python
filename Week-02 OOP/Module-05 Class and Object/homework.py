
#--------------homework-01---------------------------------------

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


#--------------------------homework-02-------------------------------

class pen:
    brand = 'Matador bol pen'

    def __init__(self,owner, brand, blackwrite, price):

        self.owner = owner 
        self.brand = brand
        self.blackwrite = blackwrite
        self.price = price

my_pen = pen('Rasel sarker','Matador high school','black',5.0)
print(my_pen.owner, my_pen.brand, my_pen.blackwrite, my_pen.price)
        


#--------------------------homework-03-------------------------------


class exam:

    def __init__(self,marks):
        self.marks = marks

        self.min_marks = 100
        self.max_marks = 100000
    def get_marks(self):
        return self.marks
    
    def specific_pass_marks(self,marks):
        if marks < 33:
            print(f'Sorry! you fail in the finall exam{self.min_marks}')
        if marks == 33:
            print(f'Congratulation! you pass in the finall exam{self.min_marks}')
        if marks>=80:
            print(f'Congratulation! you got a GPA 5.00{self.min_marks}')
                 
    
      





#--------------------------homework-04-------------------------------
#--------------------------homework-05-------------------------------
        