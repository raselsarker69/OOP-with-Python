import pymysql

db_name = "school"

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database=db_name
)


def CreateTable(tablename):
    query = f"""
                CREATE TABLE{tablename}(
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    name VARCHAR(50) NOT NULL,
                    Age INT,
                    Grade FLOAT
                );
            """
    cursor=connection.cursor()
    cursor.execute(query)

def AddStudent():
    pass


def UpdateGrade():
    pass


def IncreaseAge():
    pass


def ViewAll():
    pass


while True:
    print("""
        1. Create Table
        2. Add Student
        3. Update grade
        4. Increase Age
        5. Show all student
        6. Exit
    """)

    op = int(input("Enter your choice: "))

    if op == 1:
        tablename=input("Enter table name: ")
        CreateTable()
        print("succesfully table created")

    elif op == 2:
        AddStudent()
    elif op == 3:
        UpdateGrade()
    elif op == 4:
        IncreaseAge()
    elif op == 5:
        ViewAll()
    elif op == 6:
        break
    else:
        print("Invalid option")