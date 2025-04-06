# 1 2 3 4
# 5 6 7
# 8 9 
# 10

n=int(input("Enter the number: "))
count=1
# for i in range(n,0,-1):
#     for j in range(i):
#         print(count,end=" ")
#         count+=1
#     print()


# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(count,end=" ")
#         count+=1
#     print()



for i in range(1,n+1):
    for j in range(i,n+1):
        print(count,end=" ")
        count+=1
    print()