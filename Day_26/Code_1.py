# print the string in reverse order using negative indexing


a = input("Enter the string: ")
for i in range(-1, -len(a)-1, -1):
    print(a[i], end=" ")
