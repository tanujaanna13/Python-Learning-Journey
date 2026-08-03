"""
==========================================
        MENU-BASED CALCULATOR
==========================================

Author      : Tanuja Neela Devi
Version     : 1.0
Language    : Python

Description:
A menu-driven calculator that performs
basic and advanced mathematical operations.

==========================================
"""

import math


# ---------- Arithmetic Functions ----------

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return round(a / b, 2)


def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero is not allowed."
    return a % b


def power(a, b):
    return a ** b


def square(a):
    return a ** 2


def cube(a):
    return a ** 3


def square_root(a):
    if a < 0:
        return "Error: Square root of a negative number is not possible."
    return round(math.sqrt(a), 2)


def floor_division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a // b


def percentage(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return round((a / b) * 100, 2)


# ---------- Menu Function ----------

def display_menu():
    print("\n==========================================")
    print("         MENU-BASED CALCULATOR")
    print("==========================================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square")
    print("8. Cube")
    print("9. Square Root")
    print("10. Floor Division")
    print("11. Percentage")
    print("12. Exit")
    print("==========================================")


# ---------- Main Program ----------

def main():

    while True:

        display_menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("❌ Please enter a valid menu number.")
            continue

        if choice == 12:
            print("\n==========================================")
            print(" Thank you for using the Calculator 😊")
            print(" Have a Great Day!")
            print("==========================================")
            break

        elif choice == 7:
            try:
                num = float(input("Enter a number: "))
                print("Square =", square(num))
            except ValueError:
                print("❌ Invalid input.")

        elif choice == 8:
            try:
                num = float(input("Enter a number: "))
                print("Cube =", cube(num))
            except ValueError:
                print("❌ Invalid input.")

        elif choice == 9:
            try:
                num = float(input("Enter a number: "))
                print("Square Root =", square_root(num))
            except ValueError:
                print("❌ Invalid input.")

        elif choice in [1, 2, 3, 4, 5, 6, 10, 11]:

            try:
                num1 = float(input("Enter First Number: "))
                num2 = float(input("Enter Second Number: "))
            except ValueError:
                print("❌ Please enter numeric values only.")
                continue

            if choice == 1:
                print("Addition =", addition(num1, num2))

            elif choice == 2:
                print("Subtraction =", subtraction(num1, num2))

            elif choice == 3:
                print("Multiplication =", multiplication(num1, num2))

            elif choice == 4:
                print("Division =", division(num1, num2))

            elif choice == 5:
                print("Modulus =", modulus(num1, num2))

            elif choice == 6:
                print("Power =", power(num1, num2))

            elif choice == 10:
                print("Floor Division =", floor_division(num1, num2))

            elif choice == 11:
                print("Percentage =", percentage(num1, num2), "%")

        else:
            print("❌ Invalid choice! Please select a valid option.")


# ---------- Program Entry ----------

if __name__ == "__main__":
    main()