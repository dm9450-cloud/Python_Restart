# Find the time complexity


a=0
n=int(input("Enter a number: "))
while n>1:
    for i in range(n):
        a+=1
    n//=2
print(a)


O(n)