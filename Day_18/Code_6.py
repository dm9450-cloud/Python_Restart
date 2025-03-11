# WAP to print factorial of number

n=int(input("Enter the number: "))
a=1
fact=1
while a<=n:
    fact *=a
    a+=1
print(fact)