
class Hall:
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []


    def entry_show(self, id, movie_name, time):
        show_list = (id, movie_name, time)
        self.show_list.append(show_list)


    rows = 3
    cols = 3
    matrix = []


    for i in range(rows):
        row = []
        for j in range(cols):
            value = i * cols + j
            row.append(value)
            matrix.append(row)

    #print
    for i in range(rows):
        for j in range(cols):
           print(matrix[i][j], end=' ')
           print()



Anondo_cinama_hall = Hall(rows=10, cols=8, hall_no=1)
Anondo_cinama_hall.seats()

Anondo_cinama_hall.entry_show("1", "Prio toma", "07:00 PM")

print(Anondo_cinama_hall.show_list)
print(Anondo_cinama_hall.seats)