# Write a program where you have to take input from the user. if the number is even then print the  number and if it is odd then skip it. we will take the input from the user until user gives a negative number. 

while True:
    n=int(input("Enter the number:"))
    if n<0:
        break
    if n%2==1:
        continue 
    print(n)
