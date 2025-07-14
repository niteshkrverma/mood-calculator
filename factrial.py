# Enter a number and calculate factorial

n = int(input("Enter a number: "))
fac = 1

if n == 0:
    print("Factorial is 1")
else:
    for i in range(1, n + 1):  # <-- Loop should go till 'n'
        fac *= i
    print(f"Factorial of {n} is {fac}")
