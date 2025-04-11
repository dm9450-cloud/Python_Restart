
# WAP to print all substrings of a given string that do not contain any vowels.
s=input("Enter the string: ")
for i in range(0,len(s)):
    for j in range(i+1,len(s)+1):
        for k in "aeiou":
            if k in s[i:j]:
                break
        else:
            print(s[i:j])

