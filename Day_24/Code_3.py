# Find the time complexity


a=0
b=0
n=int(input("Enter a number: "))
m=int(input("Enter a number: "))
for i in range(n):
    a+=n
for i in range(m):
    b+=i
print(a,b)


O(n+m)

