class Star_Cinema:
    hall_list = []

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)
        self.seats[id] = [[0] * self.cols for _ in range(self.rows)]

    def book_seats(self, id, row, col):
        if id in self.seats and 1 <= row <= self.rows and 1 <= col <= self.cols:
            if self.seats[id][row - 1][col - 1] == 0:
                self.seats[id][row - 1][col - 1] = 1
                return f"Seat {row}-{col} booked for show {id}"
            else:
                return f"Seat {row}-{col} is already booked for show {id}"
        else:
            return "Invalid show ID or seat selection."

    def view_show_list(self):
        return self.show_list

    def view_available_seats(self, id):
        if id in self.seats:
            seat_matrix = self.seats[id]
            for row in range(self.rows):
                for col in range(self.cols):
                    if seat_matrix[row][col] == 1:
                        print(f"Seat {row + 1}-{col + 1}: Booked")
                    else:
                        print(f"Seat {row + 1}-{col + 1}: Available")
        else:
            print("Show not found.")

hall = Hall(3, 4, 2)
hall.entry_show('111', 'Priotoma', '10/07/2023 02:00 PM')
hall.entry_show('333', 'Sujon Maji', '10/07/2023 04:00 PM')

while True:
    print('\t1. VIEW ALL SHOW TODAY:')
    print('\t2. VIEW AVAILABLE SEATS:')
    print('\t3. BOOK TICKET:')
    print('\t4. Exit:')

    option = int(input("ENTER OPTION:"))

    if option == 1:
        print(hall.view_show_list())
    elif option == 2:
        id = input("Enter show ID: ")
        hall.view_available_seats(id)
    elif option == 3:
        id = input("Enter show ID: ")
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        result = hall.book_seats(id, row, col)
        print(result)
    elif option == 4:
        break
    else:
        print("Sorry! Please Try again.")

