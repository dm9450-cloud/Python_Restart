# Find the time complexity

a=0
n=int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        a+=1
print(a)


O(n^2)