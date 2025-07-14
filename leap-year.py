# Take input as a year and check if it is a leap year

year = int(input("Enter any year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is a leap year")
else:
    print("It is not a leap year")