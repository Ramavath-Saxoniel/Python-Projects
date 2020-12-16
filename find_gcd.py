n = int(input("To find GCD between how many numbers?\n"))
num = []
for i in range(n):
    user_input = int(input("Enter the number: "))
    num.append(user_input)
print(num)

x = min(num)
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
