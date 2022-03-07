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
        x = float(input("Enter the value of X: "))
        y = float(input("Enter the value of Y: "))
        Answer1 = x / y
        print'Quotient is: ', Answer1
            
    elif user_input == 5:
        number = int(input("Enter the number: "))
        n = float(input("Enter the power: "))
        exponential = number**n
        print number, "power", n, "is", exponential

    elif user_input == 6:
        print("Thank you!")
        break

    else:
        print'Not a valid choice'
