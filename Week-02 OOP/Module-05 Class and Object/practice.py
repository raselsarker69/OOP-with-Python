
#-------------------------------phone & class--------------------------------

class phone:
    def __init__(self, owner, brand, name, price,colour,memory) -> None:
        self.owner = owner
        self.brand = brand
        self.name = name
        self.price = price
        self.colour = colour
        self.memory = memory

    def call_phone(self):
        return f'someone call me i dont know'
    
    def __repr__(self) -> str:
        return f'owner:{self.owner},brand:{self.brand},name:{self.name},price:{self.price},colour:{self.colour},memory:{self.memory}'
        
my_phone = phone(m) 

#-------------------------------phone & class--------------------------------