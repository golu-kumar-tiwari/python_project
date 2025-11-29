#Simple Calculater

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print("Result =", x + y)

    elif ch == "2":
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print("Result =", x - y)

    elif ch == "3":
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print("Result =", x * y)

    elif ch == "4":
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        if y == 0:
            print("Cannot divide by zero")
        else:
            print("Result =", x / y)

    elif ch == "5":
        print("Calculator closed")
        break

    else:
        print("Invalid option, try again")
