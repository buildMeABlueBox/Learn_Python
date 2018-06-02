student= {"name": "Sergio", "employee_id": 123488, "feedback": None, "lastname": "Guerra"}

try:
    lastname = student["lastname"]
    numbered_lastname = 3+lastname

except KeyError as e:
    print("Error finding lastname")
except TypeError as e:
    print(f"I can't add these two together: {e}")
except Exception as e:
    print(f"Unknown Error: {e}")