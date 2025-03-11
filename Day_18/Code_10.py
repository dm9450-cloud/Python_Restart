

l=int(input("Enter the number: "))
r=int(input("Enter the number: "))
for i in range(l,r+1):
    if i%5==0:
        continue    #skip
        print(i)