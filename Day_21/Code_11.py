# Test whether a number is a prime number or not 

n=int(input("Enter the number: "))
for i in  range(2,n):
    if (n%i==0):
        print("Not a prime number")
        break
else:
    print("Prime number")