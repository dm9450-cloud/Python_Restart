# WAP to print the sum of all odd natural numbers upto n.

# n=int(input("Enter the number: "))
# sum=0
# for i in range(1,n+1):
#     if i%2!=0:
#         sum+=i
# print("Sum of all odd natural numbers ",n," is: ",sum)


# n=int(input("Enter the number: "))
# sum=0
# i=1
# while i<=n:
#     if i%2!=0:
#         sum+=i
#     i+=1
# print("Sum of all odd natural numbers ",n," is ", sum)



n = int(input("Enter the number: "))
k = (n + 1) // 2
sum = k * k
print("Sum of odd natural numbers up to", n, "is:", sum)

