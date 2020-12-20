user_input = input('Enter your name: ').upper()
print'Hello, ' + user_input

while True:
    user_input = int(input("\nEnter your choice:\n1. Addition\n2. Subtraction\n3. multiplication\n4. Division\n5. Exponential\n6. Exit\n>>>"))
    if user_input == 1:
        x = int(input("Enter the value of X: "))
        y = int(input("Enter the value of Y: "))
        Answer = x + y
        print'Answer is: ', Answer

    elif user_input == 2:
        x = int(input("Enter the value of X: "))
        y = int(input("Enter the value of Y: "))
        Answer = x - y
        print'Answer is: ', Answer

    elif user_input == 3:
        x = int(input("Enter the value of X: "))
        y = int(input("Enter the value of Y: "))
        Answer = x * y
        print'Answer is: ', Answer

    elif user_input == 4:
        user_input = input("Decimal calculation will not be done.\n1. No Problem.\n2. I need Decimal calculation.\n")
        if user_input == 1:
            x = int(input("Enter the value of X: "))
            y = int(input("Enter the value of Y: "))
            Answer1 = x // y
            Answer2 = x % y
            print'Quotient is: ', Answer1
            print'Remainder is: ', Answer2
        elif user_input == 2:
            print("Sorry, I don't do that.")

    elif user_input == 5:
        number = int(input("Enter the number: "))
        n = int(input("Enter the power: "))
        number1 = number
        for i in range(1, n):
            exponential = number*number1
            number1 = exponential
        print number, "power", n, "is", exponential

    elif user_input == 6:
        print("Thank you!")
        break

    else:
        print'Not a valid choice'
