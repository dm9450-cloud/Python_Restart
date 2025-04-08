# Find the time complexity


n=int(input("Enter the number: "))
a=0
for i in range(n):
    for j in range(n):
        a+=1

for i in range(n):
    a+=1

print(a)




O(n^2)