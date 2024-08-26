
#---------------------------------#
#                                 |
#      WELCOME TO SHOPPING APP    |
#         MD RASEL SARKER         |                          
#---------------------------------#
   

from abc import ABC,abstractmethod

class User: # korno akta class thakay abstclass k inherite korbo sudu matro tokhonay jokon oi class ar atlist akta method abstract method hobay.
    def __init__(self,id,email,password) -> None:
        self.id=id
        self.email=email
        self.password=password
        super().__init__()

class customar(User):
    def __init__(self, id, email, password) -> None:
        super().__init__(id, email, password) #ami j class ar constractor aci sei class j class k inhert kor ci cons call korci
        self.cart=[]

    def view_productos(self,products):
        print("Available Products:")
        for product in products:
            if product.in_stock>0:
                print(f"{product.name} - Price: ${product.price} - In Stock: {product.in_stock}")

    def place_order(self, product, quantity):
        if product.in_stock >= quantity:
            product.in_stock -= quantity
            self.cart.append((product, quantity))
            print(f"Added {quantity} {product.name} to your cart.")
        else:
            print(f"Sorry, {product.name} is out of stock.")

    def checkout(self):
        total_cost = 0
        for item, quantity in self.cart:
            total_cost += item.price * quantity
        print(f"Total Cost: ${total_cost}")
        print("Thank you for your order!")

class Seller(User):
    def __init__(self,id, email, password):
        super().__init__(email, password)
        self.products = []

    def publish_product(self,brand, name, price, in_stock):
        product = Product(brand,name, price, in_stock)
        self.products.append(product)
        print(f"Published {name} for sale.")

class Product:
    def __init__(self,brand, name, price, in_stock):
        self.brand=brand
        self.name = name
        self.price = price
        self.in_stock = in_stock


while True:
    print("\t1.FOR SIGN UP AS A CUSTOMAR:")
    print("\t2.FOR SIGN UP AS A SELLER:")
    print("\t3.LOGIN")

    option=int(input("ENTER YOUR OPTION:"))

    Rasel = customar("111","rasel@gmail.com","1492")
    seller = Seller("999","sarker@gmail.com","")

   