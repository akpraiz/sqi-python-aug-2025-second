def addition(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"


def subtraction(num1, num2):
    return f"{num1} - {num2} = {num1 - num2}"


def multiplication(num1, num2):
    return f"{num1} X {num2} = {num1 * num2}"


def division(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return f"{num1} / {num2} = {num1 / num2}"

menu = """Select operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
"""

print("Welcome to the simple calculator")

while True:
    print(menu)
    choice = input("Enter your choice from 1 to 5: ")

    if choice not in "12345":
        print("Invalid choice")
        break

    if choice == "5":
        print("Exiting...👋")
        break



    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == "1":
        print(addition(num1, num2))
    elif choice == "2":
        print(subtraction(num1, num2))
    elif choice == "3":
        print(multiplication(num1, num2))
    elif choice == "4":
        print(division(num1, num2))
    else:
        print("invalid choice")