lower,upper,digit,space,sc=0,0,0,0,0
s=input("Enter the string: ")
for i in s:
    if 'z'>=i>='A':
        upper+=1
    elif 'a'<=i<='z':
        lower+=1
    elif '0'<=i<='9':
        digit+=1
    elif i==' ':
        space+=1
    else:
        sc+=1