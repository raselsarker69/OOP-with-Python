from abc import ABC, abstractmethod  # abstract class ABC

class User(ABC): #abstract thakay inherrite korar method
    def __init__(self,name) -> None:
        self.name=name
        super().__init__()

class Customer(User):  #USER k inherrite korlam
    def __init__(self, name,money) -> None:
        self.wallet=money
        self.__order=None
        super().__init__(name)

    @property
    def order(self):
        return self.__order