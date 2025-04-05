# Print factorial of a number

n=int(input("Enter the number"))
fact=1
i=n
while i>=1:
    fact=fact*i
    i=i-1
print(fact)