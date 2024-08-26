class Train():
    
    def __init__(self,name,id,location,destination) -> None:
        self.name = name
        self.id = id
        self.location = location
        self.destination = destination

class Admin(Train):
    train_list = []
    passenger_list = []
    seats = {}
    
    def __init__(self,email) -> None:
        self.email = email
        
    def add_train(self,name,id,location,destination):
        new_train = Train(name,id,location,destination)
        self.train_list.append(new_train)
        print("Train added successfully.")
        seat = []
        for i in range(10):
            seat.append(['A','A','A','A'])
        self.seats[id] = seat

    def show_available_trains(self):
        print("--------------------------------------------------------------------------")
        for train in self.train_list:
            print(f'name : {train.name}, id : {train.id}, location : {train.location}, destination : {train.destination}')
        print("--------------------------------------------------------------------------")

    def show_available_seats(self,id):
        for i in self.seats[id]:
            for j in i:
                print(j,end=' ')
            print()
            
    def book_seats(self,id):
        row = int(input("Enter row : "))
        col = int(input("Enter coloumn : "))
        
        if self.seats[id][row][col] == 'X':
            print("This seat is already booked.")
        else:
            self.seats[id][row][col] = 'X'
            print("Booked successfully.")
            
    def show_all_users(self):
        for user in self.passenger_list:
            print(user.name)
    


class User():
    
    def __init__(self,name,email,password) -> None:
        self.name = name
        self.email = email
        self.password = password

admin = Admin('admin@gmail.com')

while(True):
    user_type = input("admin/user ? : ")
    if user_type == 'user' :
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        
        choice = int(input("Enter your choice : "))
        
        if choice == 1:
            email = input("Enter your email : ")
            password = input("Enter your password : ")
            
            flag = False
            for user in admin.passenger_list:
                if user.email == email and user.password == password:
                    flag = True
                    print("Welcome ", user.name)
                    while(True):
                        print("1. Show available trains.")
                        print("2. Show available seats.")
                        print("3. Book seats.")
                        print("4. Logout")

                        choice = int(input("Enter your choice : "))
                        
                        if choice == 1:
                            admin.show_available_trains()
                            
                        elif choice == 2:
                            id = int(input("Enter train id : "))
                            admin.show_available_seats(id)
                        
                        elif choice == 3:
                            id = int(input("Enter train id : "))
                            admin.book_seats(id)
                        
                        else:
                            break
            
            if flag == False:
                print("Wrong email or password.")
            
            
        elif choice == 2:
            name = input("Enter your name : ")
            email = input("Enter your email : ")
            password = input("Enter your password : ")
            
            new_user = User(name,email,password)
            admin.passenger_list.append(new_user)
            print("Registered successfully.")
        
        else:
            break
    
    elif user_type == 'admin':
        email = input("Enter your email : ")
        password = input("Enter your password : ")
        
        if email == 'admin' and password == '123':
            print("Admin successfully login.")
            while(True):
                print("1. Show all available trains.")
                print("2. Show all users.")
                print("3. Add train.")
                print("4. Logout.")
                
                choice = int(input("Enter your choice : "))
                
                if choice == 1:
                    admin.show_available_trains()
                
                elif choice == 2:
                    admin.show_all_users()
                
                elif choice == 3:
                    name = input("Enter train name : ")
                    id = int(input("Enter train id : "))
                    location = input("Enter train location : ")
                    destination = input("Enter train destination : ")

                    admin.add_train(name,id,location,destination)
                    
                elif choice == 4:
                    break
            
            
        else:
            print("Wrong email or password.")
    
    else:
        print("Invalid")