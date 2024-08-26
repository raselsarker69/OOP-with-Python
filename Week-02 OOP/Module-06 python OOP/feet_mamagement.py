
#Ena Poribohon


class Company:
    def __init__(self,name,address) -> None:
        self.name = name
        self.bus = []
        self.routes = []
        self.drivers = []
        self.counter = []
        self.managers = []
        self.supervisors = []


class driver:
    def __init__(self, name, licincs, age) -> None:
        self.name = name
        self.licince = licincs
        self.age = age

class counter:
    def __init__(self) -> None:
        pass
    def purchase_a_ticket(self, start, distination):
        pass
        

class passenger:
    pass

class supervisor:
    pass
        