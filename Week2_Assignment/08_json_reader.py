import json

with open("08_students.json", "r") as file:
    students = json.load(file)

print("Student Details:")

for student in students:
    print("Name:", student["name"])
    print("Roll Number:", student["roll_no"])
    print("Marks:", student["marks"])
    print("--------------------")