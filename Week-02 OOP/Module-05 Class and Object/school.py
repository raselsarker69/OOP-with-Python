

class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id

    def __repr__(self) -> str:
        return f'Student name: {self.name}, current_class: {self.current_class}, id: {self.id}'


class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher: {self.name}, subject: {self.subject}'
        

class School:
    def __init__(self,name) -> None:
        self.name = name
        self.teachers = []

    def add_teacher(self,name,subject):
        id = len(self.teachers) + 101
        Teacher = Teacher(name, subject, id)
        self.taechers.append(Teacher)

    def enroll(self,name,subject,fee):
        if fee < 6500:
            return 'not enough fee'
        else:
            


    def __repr__(self) -> str:
        return f'School: {self.name}, EIIN: {self.EIIN},establist: {self.establish},student: {self.student},bevag: {self.bevag}'
        
        

Rasel = Student('Rasel sarker', 10, 1)
Ranbeer = Teacher('Ranbeer', 'Algorithms', 101)
School = School('Gaibandha govt. collage','1205','1985','850','3')

print(Rasel)
print(Ranbeer)
print(School)
        