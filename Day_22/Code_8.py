# 4 3 2 1 
# 4 3 2 1 
# 4 3 2 1 
# 4 3 2 1 

n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(n,0,-1):
        print(j,end=" ")
    print()