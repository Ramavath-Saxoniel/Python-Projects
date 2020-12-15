def get_factorial(n):
	factorial = 1
	for i in range(1,n+1):
		factorial = factorial*i
	return factorial
	
print(get_factorial(10))

def get_factorial_recursion(n):
        if n==1:
                return 1
        else:
                return get_factorial_recursion(n-1)*n

print(get_factorial_recursion(10))
