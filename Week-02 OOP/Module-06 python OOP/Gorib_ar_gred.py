
class Laptop:
    def __init__(self, brand, price, colour, memory) -> None:
        self.brand = brand
        self.price = price
        self.colour = colour
        self.memory = memory

    def  run(self):
        return f'Running laptop{self.brand}'
    
    def coding(self):
        return f'Learning python and practiceing'
    
class Phone:
    def __init__(self, brand, price, colour, dual_sim) -> None:
        self.brand = brand
        self.price = price
        self.colour = colour
        self.dual_sim = dual_sim

    def run(self):
        return f'phone tipa tipi korey'
    
    def phone_call(self, number, text):
        return f'sending message to:{number} with:{text}'
    
class Camara:
    def __init__(self, brand, price, colour, pixel) -> None:
        self.brand = brand
        self.price = price
        self.colour = colour
        self.pixel = pixel

    def run(self):
        pass
    def change_lens(self):
        pass
        
        
        