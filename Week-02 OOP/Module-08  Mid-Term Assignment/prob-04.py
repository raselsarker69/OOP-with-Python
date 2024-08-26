class Star_Cinema:
    hall_list = []

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        super().__init__()

        # Initialize seats and show_list
        self.seats = []
        self.show_list = []

    def entry_show(self, id, move_name, time):
        show_info = {'Show Id': id, 'Movie Name': move_name, 'Time': time}
        self.show_list.append(show_info)

    def booking_seats(self, id, row, col):
        seat = {'Show Id': id, 'Row': row, 'Col': col}
        if seat in self.seats:
            self.seats.remove(seat)
            return seat

    def view_show_list(self):
        return self.show_list

    def view_available_seats(self, id):
        available_seats = []
        for row in range(1, self.rows + 1):
            for col in range(1, self.cols + 1):
                seat = {'Show Id': id, 'Row': row, 'Col': col}
                if seat not in self.seats:
                    available_seats.append(seat)
        return available_seats

# Initialize a Hall instance
# row = int(input("Enter The row No:"))
# col = int(input("Enter The col No:"))
# hall_no = input("Enter The Hall_No:")

# hall_name = Hall(row, col, hall_no)

while True:
    print()
    print('ENTER OPTION:')
    print('\t1. VIEW ALL SHOW TODAY:')
    print('\t2. VIEW AVILABLE SEATS:')
    print('\t3. BOOK TICKET:')
    print('\t4. EXIT:')
    print()

    option = int(input("ENTER OPTION:"))

    if option == 1:
        show_list = hall_name.view_show_list()
        for show in show_list:
            print(show)

    elif option == 2:
        show_id = input("Enter Show Id:")
        available_seats = hall_name.view_available_seats(show_id)
        for seat in available_seats:
            print(f"Available Seat: Row {seat['Row']}, Col {seat['Col']}")

    elif option == 3:
        show_id = input("Enter Show Id:")
        row = int(input("Enter Row:"))
        col = int(input("Enter Col:"))
        booked_seat = hall_name.booking_seats(show_id, row, col)
        if booked_seat:
            print(f"Seat booked: Row {booked_seat['Row']}, Col {booked_seat['Col']}")
        else:
            print("Seat is already booked.")

    elif option == 4:
        break