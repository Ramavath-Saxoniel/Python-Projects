user_input = input('Enter your name: ').upper()
print'Hello, ' + user_input


def choose_anything():
    print("Choose anything form below:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    user_input = int(input())
    if user_input == 1:
        math_addition()
    if user_input == 2:
        math_subtraction()
    if user_input == 3:
        math_multiplication()
    if user_input == 4:
        math_division()
    if user_input == 5:
        print("Thank you!")
        quit()


def math_addition():
    user_input1 = int(input("Enter the value of X: "))
    user_input2 = int(input("Enter the value of Y: "))
    Answer = user_input1 + user_input2
    print'Answer is: ', Answer


def math_subtraction():
    user_input1 = int(input("Enter the value of X: "))
    user_input2 = int(input("Enter the value of Y: "))
    Answer = user_input1 - user_input2
    print'Answer is: ', Answer


def math_multiplication():
    user_input1 = int(input("Enter the value of X: "))
    user_input2 = int(input("Enter the value of Y: "))
    Answer = user_input1 * user_input2
    print'Answer is: ', Answer


def math_division():
    user_input = input("Decimal calculation will not be done.\n1. No Problem.\n2. I need Decimal calculation.\n")
    if user_input == 1:
        user_input1 = int(input("Enter the value of X: "))
        user_input2 = int(input("Enter the value of Y: "))
        Answer1 = user_input1 / user_input2
        Answer2 = user_input1 % user_input2
        print'Quotient is: ', Answer1
        print'Remainder is: ', Answer2
    if user_input == 2:
        print("Sorry, I don't do that.")
        return choose_anything()


while True:
    choose_anything()
