# Check prime or not

n = int(input("Enter a number: "))

if n <= 1:
    print("This is not a prime number")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("This is a prime number")
    else:
        print("This is not a prime number")
