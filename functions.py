students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print() #Extra space - TODO: is there a more elegant way of prepending a new line without causing a ValueError?
    print(students_titlecase)


def add_student(name, student_id=1234):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def add_student_to_list():
    student_name = input("Enter student name:")
    student_id = input("Enter student ID: ")
    add_student(student_name, student_id)


def save_file(students):
    try:
        f = open("students.txt", "a")
        for student in students:
            f.write(f"{student['name']}\n")
        f.close()
    except Exception:
        print("Could not save file")

def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student.rstrip("\n"))
        f.close()
    except Exception:
        print("Could not read file")


read_file()
print_students_titlecase()

while True:
    add_to_list = input("Would you like to add a student? (Please type 'Yes' or 'No'): \n").upper()
    if add_to_list == "YES":
        add_student_to_list()
    elif add_to_list == "NO":
        break
    else:
        print("\nPlease only type 'Yes' and 'No'")

print_students_titlecase()
save_file(students)