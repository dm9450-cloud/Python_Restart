a=input("Enter the string: ")
for i in a:
    print(i,end=" ")
for i in range(len(a)-1,-1,-1):
    print(a[i],end=" ")