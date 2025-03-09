# WAP to print the sum of digits of a given number.

n = int(input("Enter the number: "))
sum_of_digits = 0

while n > 0:
    digit = n % 10  # Get the last digit
    sum_of_digits += digit  # Add the digit to the sum
    n = n // 10  # Remove the last digit
    
print("Sum of digits is:", sum_of_digits)




n = input("Enter the number: ")
sum_of_digits = 0

for digit in n:
    sum_of_digits += int(digit)  # Convert digit to integer and add
    
print("Sum of digits is:", sum_of_digits)
