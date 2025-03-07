
ava_candy=5

x=int(input("How many candies you want?"))
i=1
while i<=x:
    if i>ava_candy:
        print("Out of stock")
        break
    print("Candy")
    i+=1
print("Bye")