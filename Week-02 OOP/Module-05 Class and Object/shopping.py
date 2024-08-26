

class shopping:

    def __init__(self,name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item,price,quentity):
        product = {'item':item, 'price':price,'quentity':quentity}
        self.cart.append(product)

    def checkout(self,amount):
        total = 0
        for item in self.cart:
            #print(item)
            total += item['price'] * item['quentity']
        print('total price',total)
        if amount<total:
            print(f'Please provide {total-amount} more')
        else:
            extra = amount - total
            print(f'Here is your item and extra money:{extra}')


Rasel = shopping('Rasel sarker')
Rasel.add_to_cart('iPHONE', 10000,1)
Rasel.add_to_cart('Tshirt', 450,2)
Rasel.add_to_cart('Cap', 350,1)
Rasel.add_to_cart('Rolax guori', 1000,5)
print('\n')

print(Rasel.cart)

# Rasel.checkout(900)
Rasel.checkout(1900)