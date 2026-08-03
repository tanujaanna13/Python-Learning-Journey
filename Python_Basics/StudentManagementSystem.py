"""
==========================================
      STUDENT MANAGEMENT SYSTEM
==========================================

Author      : Tanuja Neela Devi
Version     : 1.0
Language    : Python

Description:
A menu-driven application to manage
student records using Python dictionaries.

Features:
- Add Student
- Display Students
- Search Student
- Update Marks
- Delete Student
- Find Topper
- Find Average Marks
- Count Students

==========================================
"""

students = {}


# ---------- Functions ----------

def add_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("❌ Student with this Roll Number already exists!")
        return

    name = input("Enter Student Name: ")

    try:
        marks = float(input("Enter Marks (0-100): "))
    except ValueError:
        print("❌ Invalid marks! Please enter numeric values.")
        return

    if marks < 0 or marks > 100:
        print("❌ Marks should be between 0 and 100.")
        return

    students[roll] = {
        "Name": name,
        "Marks": marks
    }

    print("✅ Student Added Successfully!")


def display_students():

    if not students:
        print("No Students Found!")
        return

    print("\n----------------------------------------")
    print(f"{'Roll No':<10}{'Name':<20}{'Marks'}")
    print("----------------------------------------")

    for roll, details in students.items():
        print(f"{roll:<10}{details['Name']:<20}{details['Marks']}")

    print("----------------------------------------")


def search_student():

    roll = input("Enter Roll Number: ")

    if roll in students:
        print("\nStudent Found")
        print("--------------------------")
        print("Roll No :", roll)
        print("Name    :", students[roll]["Name"])
        print("Marks   :", students[roll]["Marks"])
    else:
        print("❌ Student Not Found!")


def update_marks():

    roll = input("Enter Roll Number: ")

    if roll not in students:
        print("❌ Student Not Found!")
        return

    try:
        marks = float(input("Enter New Marks: "))
    except ValueError:
        print("❌ Invalid marks!")
        return

    if marks < 0 or marks > 100:
        print("❌ Marks should be between 0 and 100.")
        return

    students[roll]["Marks"] = marks
    print("✅ Marks Updated Successfully!")


def delete_student():

    roll = input("Enter Roll Number: ")

    if roll in students:
        del students[roll]
        print("✅ Student Deleted Successfully!")
    else:
        print("❌ Student Not Found!")


def find_topper():

    if not students:
        print("No Students Available!")
        return

    topper = max(students, key=lambda x: students[x]["Marks"])

    print("\n========== TOPPER ==========")
    print("Roll No :", topper)
    print("Name    :", students[topper]["Name"])
    print("Marks   :", students[topper]["Marks"])
    print("============================")


def average_marks():

    if not students:
        print("No Students Available!")
        return

    total = sum(student["Marks"] for student in students.values())
    average = total / len(students)

    print(f"Average Marks = {average:.2f}")


def count_students():
    print(f"Total Students = {len(students)}")


# ---------- Menu ----------

def display_menu():

    print("\n==========================================")
    print("      STUDENT MANAGEMENT SYSTEM")
    print("==========================================")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Find Topper")
    print("7. Find Average Marks")
    print("8. Count Students")
    print("9. Exit")
    print("==========================================")


# ---------- Main Function ----------

def main():

    while True:

        display_menu()

        try:
            choice = int(input("Enter Your Choice: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        if choice == 1:
            add_student()

        elif choice == 2:
            display_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            update_marks()

        elif choice == 5:
            delete_student()

        elif choice == 6:
            find_topper()

        elif choice == 7:
            average_marks()

        elif choice == 8:
            count_students()

        elif choice == 9:
            print("\n==========================================")
            print(" Thank You for Using")
            print(" Student Management System 😊")
            print("==========================================")
            break

        else:
            print("❌ Invalid Choice! Please select a valid option.")


# ---------- Program Entry ----------

if __name__ == "__main__":
    main()