#Print the sum of all odd natural numbers upto n.

n=int(input("Enter the number:"))
sum=0
i=1
while i<=n:
    if(i%2!=0):
        sum=sum+i
    i+=1
print(sum)


# n = int(input("Enter the number: "))
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 2
# print(sum)
