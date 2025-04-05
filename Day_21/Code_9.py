# print numbers from l to r . if number is divisible by 3

# l=int(input(""))
# r=int(input(""))
# i=l
# while i<=r:
#     if i%3==0:
#         break
#     print(i)
#     i=i+1



l=int(input(""))
r=int(input(""))
for i in range(l,r+1):
    if i%3==0:
        break
    print(i)
