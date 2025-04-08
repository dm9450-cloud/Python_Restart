# Print the string in reverse order
a=input("Enter the string: ")
for i in a:
    print(i,end=" ")
print()
for i in range(len(a)-1,-1,-1):
    print(a[i],end=" ")