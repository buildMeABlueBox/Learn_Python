student= {"name": "Sergio", "employee_id": 123488, "feedback": None, "lastname": "Guerra"}

try:
    lastname = student["lastname"]
    numbered_lastname = 3+lastname

except KeyError:
    print("Error finding lastname")
except TypeError:
    print("I can't add these two together!")