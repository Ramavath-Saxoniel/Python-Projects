def get_gcd(a, b):
        least = min(a, b)
        for i in range(1, least+1):
                if a==0 or b==0:
                        gcd=0
                if a%i==0 and b%i==0:
                        gcd=i
        return gcd
print(get_gcd(20, 24))
