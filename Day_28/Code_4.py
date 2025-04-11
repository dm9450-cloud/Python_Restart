


s=input("Enter the string: ")
m=0
c=0
for i in range(0,len(s)):
    for j in range(i,len(s)):
        c+=1
        if s[j] in "aeiou":
            break
        m=max(m,c)
        print(s[i:j],end=" ")
print(m)
