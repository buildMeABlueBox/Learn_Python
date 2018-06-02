student={
    "name": "Sergio",
    "employee_id": 123488,
    "feedback": None
}

try:
    lastname = student["lastname"]
except KeyError:
    print("Error finding lastname")