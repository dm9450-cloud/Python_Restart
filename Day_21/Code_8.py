# Print the multiplication of digits of a given number

n=int(input("Enter the number:"))
mul=1
while n>0:
    last_digit=n%10
    mul=mul*last_digit
    n=n//10
print(mul)



# If input is 0, output will be 1, which may be unexpected. You can handle that like this:


# n = int(input("Enter the number: "))
# if n == 0:
#     print(0)
# else:
#     mul = 1
#     while n > 0:
#         last_digit = n % 10
#         mul *= last_digit
#         n //= 10
#     print(mul)