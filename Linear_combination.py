a = int(input("Enter the number: "))
b = int(input("Enter the number: "))

if b>a:
    temp = a
    a = b
    b = temp
num1 = a
num2 = b

def get_gcd(a, b, num1, num2):
    n=0
    q = []
    while (b):
        q.append(a//b)
        a, b = b, a%b
    q.pop()
    n = len(q)
    gcd = a
    for i in range(n):
        q[i] = -1*q[i]
    if n==0:
        print gcd, " = ((1)*", num1, ") + ((", -1*((num1//num2)-1), ")*", num2, ")"
    elif n==1:
        print gcd, " = ((1)*", num1, ") + ((", q[n-1], ")*", num2, ")"
    elif n>1:
        a = 1
        b = q[n-1]
        for i in range(1, n):
            if i%2!=0:
                a = a+(b*q[n-(i+1)])
            else:
                b = b+(a*q[n-(i+1)])
        if n%2!=0:
            print gcd, " = ((", a, ")*", num1, ") + ((", b, ")*", num2, ")"
        else:
            print gcd, " = ((", a, ")*", num2, ") + ((", b, ")*", num1, ")"
    return gcd

gcd = get_gcd(a, b, num1, num2)

print "GCD = ", gcd
