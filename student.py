students = []

class Student:
    school = "Springfield Elementary"

    def __init__(self, name, student_id=1234):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return f"Student: {self.name}"

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return f"This is a student at {self.school}"