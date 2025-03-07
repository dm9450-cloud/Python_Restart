# WAP to print first 50 fibonacci numbers.

a,b=0,1
print(a,b,end=" ")
for _ in range(48):
    next_fib=a+b
    print(next_fib,end=" ")
    a,b=b,next_fib