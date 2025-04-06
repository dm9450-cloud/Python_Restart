# WAP that finds the prime numbers from x to y.

x=int(input("Enter first number: "))
y=int(input("Enter second number: "))

for a in range(x,y+1):
    for i in range(2,a):
        if a%i==0:
            # print(a,"is not a prime number")
            break
    else:
        print(a,"is prime number")
    




# n=int(input("Enter the number: "))
# for i in range(2,n-1):
#     if n%i==0:
#         print("Not a prime number")
#         break
# else:
#     print("Prime number")