name = input("Enter your name: ").upper()
print("Hi " + name + ", Now I am going to find LCM and GCD of n numbers.")

while True:
    user_input = int(input("\nEnter your choice:\n1. Find LCM\n2. Find GCD\n3. Exit\n>>>"))

    if user_input == 1:
        n = int(input("To find LCM between how many numbers?\n"))
        num = []
        for i in range(n):
            user_input = int(input("Enter the number: "))
            num.append(user_input)
        print(num)
        def get_gcd(a, b):
            while (b):
                a, b = b, a%b
            return a
        def find_lcm(num):
            lcm = num[0]
            for i in range(1,len(num)):
                lcm = lcm*num[i]//get_gcd(lcm, num[i])
            return lcm
        print "LCM = ", find_lcm(num)

    elif user_input == 2:
        n = int(input("To find GCD between how many numbers?\n"))
        num = []
        for i in range(n):
            user_input = int(input("Enter the number: "))
            num.append(user_input)
        print(num)
        num1 = num[0]
        num2 = num[1]
        def get_gcd(a, b):
            while (b):
                a, b = b, a%b
            return a
        gcd = get_gcd(num1, num2)
        for i in range(2, len(num)):
            gcd = get_gcd(gcd, num[i])
        print "GCD = ", gcd

    elif user_input == 3:
        break

    else:
        print'Not a valid choice'

