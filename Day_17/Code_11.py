# WAP to print the powers of 2 that  are smaller then number n.


n = int(input("Enter the number: "))

power = 1
for i in range(n):
    if power < n:
        print(power)
        power *= 2
    else:
        break



n = int(input("Enter the number: "))

power = 1
while power < n:
    print(power)
    power *= 2
