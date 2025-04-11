# Print all the substring of a string 

s=input("Enter the string: ")

for i in range(0,len(s)):
    for j in range(i+1,len(s)+1):
        print(s[i:j])