
class Book:
    def __init__(self, id, name, authar, quentity, price) -> None:
        self.id = id
        self.name = name
        self.authar = authar
        self.quentity = quentity 
        self.price = price
        #ai book prepare koray fallam

class User:
    def __init__(self, id, name, password) -> None:
        self.id = id
        self.name = name
        self.password = password
        self.borrewedBooks = []
        self.returnedBooks = []

class Libaray:
    def __init__(self,name) -> None:
        self.name = name
        self.user = []
        self.books = []

    def addbook(self,id, name, quentity):
        book=Book(id,name,quentity)
        self.books.append(book)
        print(f'{book.name} added succesfully !\n')

    def addUser(self,id, name, password):
        user=User(id,name,password)
        self.users.append(user)
        return user
    

    def borrowedBook(self,user,token):
        for book in self.books:
            if book.name==token:
                if book in user.borrewedBooks:
                    print("Already borrowed!\n")
                    return
                    print("Borrowed book succesfully!\n")

                elif book.quentity==0:
                    print("No Copy Avilable!\n")
                    return
            
            user.borrowedbooks.append(book)
            book.quentity -=1
            return
        print(f"Not Found Any Book with name{token}!\n")


    def returnBook(self,user,token):
        for book in self.books:
            if book.name==token:
                if book in user.borrewedBooks:
                    book.quentity+=1
                    user.returnBooks.append(book)
                    user.borrowedBooks.remove(book)
                    print("Returned book succesfully!\n")

                elif book.quentity==0:
                    print("No Copy Avilable!\n")
                    return
            
            user.borrowedbooks.append(book)
            book.quentity -=1
            return
        print(f"Not Found Any Book with name{token}!\n")



bsk = Libaray('Mahbubul hasan shanto')
admin = bsk.addUser(1000,"admin",3333)
rasel = bsk.addUser(15,'rasel','9999')
cpbook = bsk.addbook(15,'cpbook','8888')

currentUser = None

while True:
    if currentUser==None:
        print("No loggen in user\n")

        option=input("Login or Register(L\R) :")

        if option=="L":
            id=input("Enter Id: ")
            password=input("Enter Password: ")

            match=False
            for user in bsk.users:
                if user.id==id and user.password==password:
                    currentUser=user
                    match=True

                if match==False:
                    print("No user Found !\n")


        elif option=="R":
            id=input("Enter Id: ")
            name=input("Enter name:")
            password=input("Enter Password: ")

            match=False
            for user in bsk.users:
                if user.id==id:
                    print("user already exists!\n")
                

            user=bsk.adduser(id,name,password)
            currentUser=user

        else: 
            currentUser=admin

            if currentUser.name=="admin":
                print("Options:\n")
                print("1:Add book")
                print("1:Add user")
                print("1:Show all books")
                print("1:Logout")

                ch=int(input("Enter option"))

            elif ch==1:
                id=int(input("Enter book id: "))
                name=int(input("Enter book name: "))
                quen=int(input("Enter no of book: "))

                bsk.addbook(id,name,quen)

            elif ch==3:
                for book in bsk.books:
                    print(f'{book.id}\t{book.name}\t{book.quentity}')
                    print("\n")
           
            elif ch==4:
                currentUser==None
        
    else:
        print("Options:\n")
        print("1: Borrow Book")
        print("2: Return Book")
        print("3: Show Borrowed Book")
        print("4: Show History")
        print("5: Logout")

        ch=int(input(("Enter Option:")))

        if ch==1:
            name=int(input("Enter Book name:"))
            bsk.borrowedBook(currentUser.name)

        elif ch==2:
            name=int(input("Enter Book name:"))
            bsk.borrowedBook(currentUser.name)

        elif ch==3:
            print("\n Borrow Book:\n")
            for book in currentUser.borrewedBooks:
                print(f'{book.id}\t{book.name}\t{book.quentity}')
            print("\n")

        elif ch==4:
            print("\nHistory:\n")
            for book in currentUser.returnedBooks:
                print(f'{book.id}\t{book.name}\t{book.quentity}')
            print("\n")

        elif ch==5:
            currentUser=None







        
        


        