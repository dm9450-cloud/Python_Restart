# checks whether a string is palindrome or not

s=input("Enter the string: ")
# a=s[::-1]
# a=s[0,len(s):-1]
# a=s[len(s)-1:-1:-1]
a=s[len(s)-1::-1]
if a==s:
    print("String is palindrome")
else:
    print("String is not palindrome")