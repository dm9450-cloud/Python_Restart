# Display the length of the longest substring having only consonants.


s=input("Enter the string: ")
m=0
c=0
for i in range(0,len(s)):
    if s[i] in "aeiou":
        c+=0
    else:
        c+=1
    m=max(m,c)
        # print(s[i:j],end=" ")
print(m)