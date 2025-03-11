# WAP to print the sum of digits of a given number

n=int(input("Enter the number: "))
sum_of_digit=0
while n>0:
    rem=n%10
    sum_of_digit += rem
    n//=10
print("Sum of digit is: ",sum_of_digit)