# Write a code to print all the values from 1 to 100. Skip the numbers which are divisible by 3 or 5

i=1
while i<=100:
    if i%3==0 or i%5==0:
        i=i+1
        continue
    print(i)
    i=i+1