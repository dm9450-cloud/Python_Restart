s=input("Enter the string: ")
i=0
j=len(s)-1

while i<j:
    if s[i]!=s[j]:
        print("Not a palindrome")
        break
    else:
        i+=1
        j-=1
else:
    print("Palidrome....")