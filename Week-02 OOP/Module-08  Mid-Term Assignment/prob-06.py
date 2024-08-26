class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)

    def __init__(self):
        pass

class Hall(Star_Cinema):
    def __init__(self, hall_name):
        super().__init__()
        self.hall_name = hall_name

    def entry_hall(self):
        Star_Cinema.entry_hall(self)

class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)

    def __init__(self):
        pass

class Hall(Star_Cinema):
    def __init__(self, hall_name):
        super().__init__()
        self.hall_name = hall_name

    def entry_hall(self):
        Star_Cinema.entry_hall(self)

class Show:
    def __init__(self, id, movie_name, time):
        self.id = id
        self.movie_name = movie_name
        self.time = time

class Hall(Star_Cinema):
    def __init__(self, hall_name):
        super().__init__()
        self.hall_name = hall_name

    def entry_hall(self):
        Star_Cinema.entry_hall(self)

class Show:
    def __init__(self, id, movie_name, time):
        self.id = id
        self.movie_name = movie_name
        self.time = time

class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)

    def __init__(self):
        pass

class Hall(Star_Cinema):
    def __init__(self, hall_name):
        super().__init__()
        self.hall_name = hall_name

    def entry_hall(self):
        Star_Cinema.entry_hall(self)

class Show:
    def __init__(self, id, movie_name, time):
        self.id = id
        self.movie_name = movie_name
        self.time = time

class Hall(Star_Cinema):
    def __init__(self, hall_name):
        super().__init__()
        self.hall_name = hall_name
        self.show_list = []

    def entry_hall(self):
        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show = Show(id, movie_name, time)
        self.show_list.append(show)

    def book_seats(self, id, seats_to_book):
        if id in self.seats:
            for row, col in seats_to_book:
                if self.seats[id][row][col] == 0:
                    self.seats[id][row][col] = 1
                else:
                    print(f"Seat {row + 1}-{col + 1} is already booked.")
        else:
            print("Invalid hall ID.")

    def view_show_list(self):
        for show in self.show_list:
            print(f"ID: {show.id}, Movie: {show.movie_name}, Time: {show.time}")

    def view_available_seats(self, id):
        if id in self.seats:
            for row, seats_row in enumerate(self.seats[id]):
                for col, seat in enumerate(seats_row):
                    status = "Booked" if seat == 1 else "Available"
                    print(f"Seat {row + 1}-{col + 1}: {status}")
        else:
            print("Invalid hall ID.")

# Example usage:
hall1 = Hall("Hall 1")
hall1.entry_show(1, "Movie A", "10:00 AM")
hall1.entry_show(2, "Movie B", "2:00 PM")
hall1.view_show_list()

hall1.seats = {}
hall1.seats[1] = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
hall1.seats[2] = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

hall1.book_seats(1, [(0, 0), (0, 1)])
hall1.book_seats(2, [(1, 1), (2, 2)])

hall1.view_available_seats(1)
hall1.view_available_seats(2)