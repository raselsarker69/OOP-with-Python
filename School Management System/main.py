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
                CREATE TABLE {tablename} (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    name VARCHAR(50) NOT NULL,
                    Age INT,
                    Grade FLOAT
                );
            """
    cursor = connection.cursor()
    cursor.execute(query)

def AddStudent(tablename, name, age, grade):
    query = f"""
                INSERT INTO {tablename}(name, age, grade)
                VALUES(%s, %s, %s)
            """
    cursor = connection.cursor()
    cursor.execute(query, (name, age, grade))
    connection.commit()
    print("SUCCESSFULLY INSERTED STUDENT INFO")

def UpdateGrade(id,grade):
    query = f"""
                UPDATE Students
                SET grade = %s
                WHERE id = %s
            """
    cursor = connection.cursor()
    cursor.execute(query,(grade,id))
    connection.commit()
    print("SUCCESSFULLY UPDATED")

def IncreaseAge(id,val):
    query = f"""
          SELECT Age FROM Students WHERE id=%s
        """
    cursor = connection.cursor()
    cursor.execute(query, (id))
    age = cursor.fetchone()

    # print(age)
    # print(type(age))
    # print(age[0])

    newAge = age[0]+val
    cursor.execute("""
                   UPDATE Students
                   SET age = %s
                   WHERE id = %s
                """,(newAge,id))
    connection.commit()
    print("SUCCESSFULLY UPDATED")

def ViewAll(id):
    query = f"""
                SELECT * FROM Students
            """
    cursor = connection.cursor()
    cursor.execute(query)

    alldata = cursor.fetchall()
    print(alldata)

    print("\n+----------------------+")
    print("ID---NAME----AGE---GRADE")
    print("+-----------------------+")
    for student in alldata:
        id,name,age,grade=student #unpack
        print(f"{id}-{name}--{age}--{grade}\n")


while True:
    print("""
        1. Create Table
        2. Add Student
        3. Update grade
        4. Increase Age
        5. Show all student
        6. Exit
    """)

    op = int(input("ENTER YOUR CHOICE: "))

    if op == 1:
        tableName = input("ENTER TABLE NAME: ")
        CreateTable(tableName)
        print("SUCCESSFULLY CREATED")

    elif op == 2:
        tableName = input("ENTER TABLE NAME: ")
        name=input("ENTER STUDENT NAME: ")
        age=int(input("ENTER STUDENT AGE: "))
        grade=float(input("ENTER STUDENT GRADE: "))
        AddStudent(tableName,name,age,grade)
        
    elif op == 3:
        id=int(input("ENTER STUDENT ID: "))
        grade=int(input("ENTER NEW GRADE: "))
        UpdateGrade(id,grade)
    elif op == 4:
        id=int(input("ENTER STUDENT ID: "))
        val=int(input("ENTER VALUE TO INCREASE: "))
        IncreaseAge(id,val)
    elif op == 5:
        id=int(input("ENTER STUDENT id: "))
        ViewAll(id)
    elif op == 6:
        break
    else:
        print("Invalid option")