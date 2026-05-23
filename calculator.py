print("SMART CALCULATOR")

while True:

    print("\n========== MENU ==========")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    ch = input("Enter Choice: ")

    if ch == "5":

        print("Calculator Closed")

        break

    elif ch == "1" or ch == "2" or ch == "3" or ch == "4":

        a = float(input("Enter First Number: "))

        b = float(input("Enter Second Number: "))

        if ch == "1":

            print("Addition =", a + b)

        elif ch == "2":

            print("Subtraction =", a - b)

        elif ch == "3":

            print("Multiplication =", a * b)

        elif ch == "4":

            if b == 0:

                print("Division By Zero Not Possible")

            else:

                print("Division =", a / b)

    else:

        print("Invalid Choice")
