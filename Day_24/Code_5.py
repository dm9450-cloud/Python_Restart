# Find the time complexity


a=0
n=int(input("Enter the number: "))
while n>1:
    a+=1
    n//=2
print(a)


O(logn)