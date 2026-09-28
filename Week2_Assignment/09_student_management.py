import csv
import os

FILE_NAME = "students.csv"


def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Roll No", "Name", "Marks"])


def add_student():
    roll_no = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll_no, name, marks])

    print("Student added successfully!")


def display_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        print("\n--- STUDENT DETAILS ---")

        for row in reader:
            print(row)


def search_student():
    roll_no = input("Enter Roll No to search: ")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == roll_no:
                print("Student found!")
                print("Roll No:", row[0])
                print("Name:", row[1])
                print("Marks:", row[2])
                return

    print("Student not found.")


def delete_student():
    roll_no = input("Enter Roll No to delete: ")

    students = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] != roll_no:
                students.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(students)

    print("Student deleted successfully!")


create_file()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")