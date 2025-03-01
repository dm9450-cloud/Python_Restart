# WAP to find the largest value

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

m=b
if m<c:
    m=c
if m<a:
    m=a
print(m)