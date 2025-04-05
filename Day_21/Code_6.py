# Print the powers of 2 that are smaller then number n
n=int(input("Enter the number: "))
sum=0
p=1
while p<=n:
    sum=sum+p
    print(p)
    p=p*2
print(sum)