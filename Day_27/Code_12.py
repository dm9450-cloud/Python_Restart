# Take a string as input the numbers of uppercase, lowercase characters, digits and alphabets in it.
# Also print the number of spaces and special characters in it.

# lower=upper=digit=0
lower,upper,digit,space,sc=0,0,0,0,0
s=input("Enter the string: ")
for i in s:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    elif i.isdigit():
        digit+=1
    elif i.isspace():
        space+=1
    else:
        sc+=1

print("Alphabets: ",lower+upper)
print("Uppercase: ",upper)
print("Lowercase: ",lower)
print("Digits: ",digit)
print("Spaces: ",space)
print("Special characters: ",sc)

# s="Aa1@b2c34"

# 4 Alphabet
# digit = 4
# lowercase = 3
# uppercase = 1

# Enter the string: A@a13dn &6B
# Alphabets:  5
# Uppercase:  2
# Lowercase:  3
# Digits:  3