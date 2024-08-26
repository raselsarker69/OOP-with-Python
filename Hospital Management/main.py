import pymysql

db_name="hospital"

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database=db_name
)

def CreateTable(tableName):
    query = f"""
        CREATE TABLE {tableName} (
            Reg_No INT PRIMARY KEY AUTO_INCREMENT,
            HospitalName VARCHAR(50) NOT NULL,
            Location VARCHAR(50) NOT NULL,
            ContactNumber VARCHAR(15) UNIQUE,
            Email VARCHAR(50) UNIQUE,
            Website VARCHAR(50) NOT NULL,
            EmergencyServicesAvailability VARCHAR(50) NOT NULL
        )
    """
    cursor = connection.cursor()
    cursor.execute(query, tableName)
    connection.commit()  
    print("Successfully Created")


def DoctorInfo(DoctorID, DoctorName, email,Specialization):
    query = """
                INSERT INTO Doctor (DoctorID, DoctorName, Email) 
                VALUES (%s, %s, %s, %s)
            """
    cursor = connection.cursor()
    cursor.execute(query, (DoctorID, DoctorName, email))
    connection.commit()
    print("Successfully Created")


def PatientInfo(Patientid, patiendname, phone, problem):
    query = """
                INSERT INTO Patient (PatientID, PatientName, Phone, problem) 
                VALUES (%s, %s, %s, %s)
            """
    cursor = connection.cursor()
    cursor.execute(query, (Patientid, patiendname, phone, problem))
    connection.commit()
    print("Successfully patient admitted")


def AvilableDoctor():
    pass

def Addpatient(patientName,age,E_phone,Ward):
        query = """
                INSERT INTO Patient(patientName,age,E_phone,Ward)
                VALUES
                (%s,%s,%s,%s)
            """
        cursor = connection.cursor()
        cursor.execute(query,(patientName,age,E_phone,Ward))
        connection.commit()
        print("Successfully patient addmitted")
   

def ReleasePatient(patientname, payment):
    query = """
                UPDATE Patient
                SET payment = %s
                WHERE patientname = %s
            """
    cursor = connection.cursor()
    cursor.execute(query, (payment, patientname))
    connection.commit()
    print("Successfully updated payment for patient")

def Appointment(patientName, age, phone, Ward,Date):
    query = """
            INSERT INTO Appointment (PatientName, Age, EmergencyPhone, WardUnit,Date)
            VALUES (%s, %s, %s, %s, %s)
        """
    cursor = connection.cursor()
    cursor.execute(query, (patientName, age, phone, Ward, Date))
    connection.commit()
    print("Successfully Appointment received")


def ViewAll():
    query = "SELECT * FROM Hospital"

    cursor = connection.cursor()
    cursor.execute(query)
    hospitals = cursor.fetchall()

    if hospitals:
        for hospital in hospitals:
            print(hospital)
    else:
        print("No hospitals found.")



while True:
    print("""
        1. Create Table
        2. Doctor Info
        3. Patient Info
        4. Add Doctor
        5. Add Patient
        6. Release Patient
        7. Appointment
        8. Show All Registered patient
        9. Exit
    """)

    op=int(input("ENTER YOUR CHOICE: "))

    if op==1:
        tableName=input("Enter Table Name: ")
        CreateTable(tableName)
        print("Successfully Created")

    elif op==2:
        DoctorID =int(input("Enter Doctor Id: "))
        DoctorName=input("Enter Doctor Name: ")
        email=input("Enter Email Id: ")
        Specialization = input("Enter Specialization: ")
        DoctorInfo(DoctorID,DoctorName,email,Specialization)
        

    elif op==3:
        Patientid = int(input("Enter patient id: "))
        patiendname = input("Enter patient Name: ")
        phone = int(input("Enter phone number: "))
        PatientInfo(Patientid,patiendname,phone)

    elif op==4:
        AvilableDoctor()

    elif op==5:
        patientName = input("Enter Patient Name: ")
        age = int(input("Enter patient age: "))
        E_phone = input("Enter phone Number: ")
        Ward = input("Enter ward Name: ")
        Addpatient(patientName,age,E_phone,Ward)

    elif op == 6:
        patientname = input("Enter patient name: ")
        payment = input("Enter payment status: ")

        if payment.lower() == "yes":
            doctor = input("Enter doctor's name for permission: ")

            if doctor.lower() == "parmit":  
                print("Successfully released patient")
            else:
                print("No release for patient. Incorrect doctor's name.")
        else:
            print("Payment due!\n")

    elif op==7:
        patientName=input("Enter Patient Name: ")
        age=int(input("Enter Age: "))
        phone=int(input("Enter phone Number: "))
        Ward=input("Enter ward Name: ")
        Date=int(input("Enter Date: "))
        Appointment(patientName,age,phone,Ward,Date)

    elif op==8:
        ViewAll()
        
    elif op==9:
        connection.close()
        break
    else:
        print("Invalid option")
    