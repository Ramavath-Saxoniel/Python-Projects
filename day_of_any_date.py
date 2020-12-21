date = int(input("Enter the date: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

if month<3:
    month = month+12
    year = year-1
a = date + (2*month) + (6*(month+1)/10) + year + (year/4) + (year/400) - (year/100) + 1
f = a%7
days = ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY']
print days[f]
