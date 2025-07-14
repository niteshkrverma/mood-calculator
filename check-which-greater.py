# Take 3 numbers as input and check which one is greater and also check if all are equal

x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))

if x == y == z:
    print("All numbers are equal")
elif x >= y and x >= z:
    print("1st Number is greatest")
elif y >= x and y >= z:
    print("2nd Number is greatest")
else:
    print("3rd Number is greatest")