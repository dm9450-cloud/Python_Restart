# Display the length of the longest substring having only consonants.


s=input("Enter the string: ")
m=0
for i in range(0,len(s)):
    for j in range(i+1,len(s)+1):
        for k in "aeiou":
            if k in s[i:j]:
                break
        else:
            m=max(m,len(s[i:j]))
            print(s[i:j])
print(m)
