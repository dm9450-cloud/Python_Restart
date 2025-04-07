# Find the time complexity


a=0
n=int(input("Enter a number: "))
i,j=1,1
while i<n:
    while j<n:
        j+=1
        a+=1
    i+=1
print(a)


