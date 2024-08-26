from abc import ABC , abstractclassmethod
from datetime import datetime

class Ride_sharing:
    def __init__(self,company_name) -> None:
        self.company_name=company_name
        self.riders=[]
        self.drivers=[]
        self.rides=[]

    def add_rider(self,rider):
        self.riders.append(rider)

    def add_driver(self,rider):
        self.drivers.append(Driver)

    def __repr__(self) -> str:
        return f'{self.company_name} with riders:{len(self.riders)} and drivers:{len(self.drivers)}'
        
class User(ABC):
    def __init__(self,name,email,nid) -> None:
        self.name=name
        self.email=email
        #TODO :set user id dynamically

        self._id=0
        self._nid=nid
        self.wallet=0
        
    @abstractclassmethod
    def display_profile(self):
        raise NotImplementedError
    
   
    
class Rider(User):
    def __init__(self, name, email, nid,current_location,initiale_amount) -> None:
        self.current_ride=None
        self.wallet=initiale_amount
        self.current_location=current_location #manay location update kortay parbo
        super().__init__(name, email, nid)

    def display_profile(self):
        print(f'Rider: with name:{self.name} and email:{self.email}')

    def load_cash(self,amount):
        if amount > 0:
            self.wallet += amount

    def update_location(self,current_location):
        self.current_location=current_location

    def requst_ride(self,location,destination):
        if not self.current_ride:
            
            #TODO:set ride properly
            #TODO: set current ride properly

            ride_requst=Ride_requst(self,destination)
            ride_matcher=Ride_matching
            self.current_ride= ride_matcher.find_driver(ride_matcher)

class Driver(User):
    def __init__(self, name, email, nid,current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location=current_location
        self.wallet=0

    def display_profile(self):
        print(f'Driver: with name:{self.name} and emil:{self.email}')

    def accept_ride(self,ride):
        ride.set_driver(self)


class Ride:
    def __init__(self,start_location,end_location) -> None:
        self.start_location=start_location
        self.end_location=end_location
        self.driver=None
        self.rider=None
        self.start_time=None
        self.end_time=None
        self.estimated_fare=None

    def driver(self,driver):
        self.driver=driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self,rider,amount):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare
        
class Ride_requst:
    def __init__(self,rider,end_location) -> None:
        self.rider=rider
        self.end_location=end_location

class Ride_matching:
    def __init__(self) -> None:
        self.available_drivers=[]

    def find_driver(self,ride_requst):
        if len(self.available_drivers) > 0:
            #TODO : find the closest driver of the rider
            driver=self.available_drivers[0]
            ride=Ride(ride_requst.start_location,ride_requst.end_location)
            driver.accept_ride(ride)
            return ride
        
class vehicle(ABC):
    speed={
            'car':150,
           'bike':80,
           'CNG':50,
           
        }
    def __init__(self,vehicle_type,license_plate,rate) -> None:
        self.vehicle_type=vehicle_type
        self.license_plate=license_plate
        self.rate=rate
        self.status='Avilable'
       

    @abstractclassmethod
    def start_drive(self):
        pass

class car(vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

    def start_drive(self):
        self.status='unavilable'

class Bike(vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

    def start_drive(self):
        self.status='unavilable'
    
# cheack the class integration

neya_jau=Ride_sharing('Neya jau')
Rasel=Rider('rasel','rasel@sarker',20228189,'Gaibandha','2000')
neya_jau.add_rider(Rasel)

Sarker=Rider('sarker','sarker@sarker',20238989,'Feelesthan','3000')
neya_jau.add_rider(Sarker)
print(neya_jau)