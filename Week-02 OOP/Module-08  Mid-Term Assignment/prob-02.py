class Star_Cinema:
    hall_list = []

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = []
        self.show_list = []

    def entry_show(self, id, move_name, time):
        show_info = (id, move_name, time)
        self.show_list.append(show_info)

    def book_seats(self, id, row, col):
        seat = (id, row, col)
        if seat in self.seats:
            return seat

    def view_show_list(self):
        return self.show_list

    def view_available_seats(self, id):
        for row in range(1, self.rows + 1):
            for col in range(1, self.cols + 1):
                seat = (id, row, col)
                self.seats.append(seat)
        return self.seats

# Create a Hall object outside the loop
hall = Hall(2, 3, 1)

while True:
    print('ENTER OPTION:')
    print('\t1. VIEW ALL SHOW TODAY:')
    print('\t2. VIEW AVAILABLE SEATS:')
    print('\t3. BOOK TICKET:')
    print('\t4. Exit:')
    print()

    option = int(input("Enter option:"))

    if option == 1:
        print(hall.view_show_list())

    elif option == 2:
        id = input("Enter show ID: ")
        available_seats = hall.view_available_seats(id)
        print("Available Seats:", available_seats)

    elif option == 3:
        id = input("Enter show ID: ")
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        booked_seat = hall.book_seats(id, row, col)
        if booked_seat:
            print("Seat booked:", booked_seat)
        else:
            print("Seat is not available.")
            
    elif option == 4:
        break
    else:
        print("Invalid option. Please choose a valid option.")