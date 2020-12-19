n = int(input("To find maximum and minimum between how many numbers?\n"))
num = []
for i in range(n):
    user_input = int(input("Enter the number: "))
    num.append(user_input)
print num

maximum = num[0]
minimum = num[0]
for i in range(1, n):
    if num[i] > maximum:
        maximum = num[i]
    if num[i] < minimum:
        minimum = num[i]
print'Maximum = ', maximum
print'Minimum = ', minimum
