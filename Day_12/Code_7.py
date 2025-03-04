
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
ch=input("Enter a symbol: ")
if ch=='+':
    print(a+b)
elif ch=='-':
    print(a-b)
elif ch=='*':
    print(a*b)
elif ch=='/':
    if b==0:
        print("Undefined")
    else:
        print(a/b)
else:
    print("Invalid operator")