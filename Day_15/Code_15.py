# WAP to check a given number is prime or not 

# Input from user
num = int(input("Enter a number: "))

# Prime check logic
if num < 2:
    print(num, "is NOT a Prime number.")
else:
    is_prime = True  # Assume number is prime
    for i in range(2, int(num**0.5) + 1):  # Check divisibility up to √num
        if num % i == 0:
            is_prime = False  # If divisible, mark as not prime
            break  # Exit loop early

    if is_prime:
        print(num, "is a Prime number.")
    else:
        print(num, "is NOT a Prime number.")
