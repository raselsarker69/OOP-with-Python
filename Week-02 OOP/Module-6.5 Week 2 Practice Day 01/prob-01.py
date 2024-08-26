
#----------------------------Product class-----------------------------


class Product:
    def __init__(self,name, brand, price, colour, origin) -> None:
        self.name = name
        self.brand = brand
        self.price = price
        self.colour = colour
        self.origin = origin
    
    def run(self):
        return f'running mobile phone{self.brand}'
    
class mobile_phone:
    def __init__(self, memory, dual_sim) -> None:
        self.memory = memory
        self.dual_sim = dual_sim

    def playing_vedio(self):
        return f'imformative news collaction'
    
class Bike(Product):
    def __init__(self, name, brand, price, colour, origin,cc) -> None:
        self.cc = cc
        super().__init__(name, brand, price, colour, origin)
    def __repr__(self) -> str:
        return f'bike: {self.brand} {self.price} {self.cc}'

    def rid(self):
        return f'running very good in highway road'
    
class book(Product):
    def __init__(self, name, brand, price, colour, origin,writter) -> None:
        self.writter = writter
        super().__init__(name, brand, price, colour, origin)
  
    def __repr__(self) -> str:
        return f'book: {self.brand} {self.price} {self.writter}'
    
    
my_bike = Bike('4b','tvs',120000,'black','America',150)
my_book = book('Algorithms','dimik',320,'white','Bangladesh','Rasel sarker')
print(my_bike.price)
print(my_bike)
print(my_bike.rid())

print(my_book.writter)
print(my_book)

        
#----------------------------shop class-----------------------------
        
        
        

        