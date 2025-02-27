class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

class Student(Person):
    def __init__(self, name, age, email, student_id):
        super().__init__(name, age, email)
        self.student_id = student_id

