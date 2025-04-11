# Display the length of the longest substring having only consonants.
s=input("Enter the string: ")
n=len(s)
ans=0
c=0
for i in range(n):
    if(s[i] in "AEIOUaeiou"):
        ans+=c*(c+1)/2
        c=0
    else:
        c+=1
ans+=c*(c+1)/2
print(ans)