# Check Prime
# Write a program that inputs a positive integer N. It should then output a message indicating whether the number is a prime number or not.

# Input Format
# A single line containing the integer N

# Output Format
# Print a string, either "N is a prime number" or "N is not a prime number" (without quotes), depending on whether N is prime or not.

# Example 1
# Input

# 5
# Output

# 5 is a prime number
# Explanation

# 5 is only divisible by itself and 1, hence it's a prime number.

# Example 2
# Input

# 10
# Output

# 10 is not a prime number
# Explanation

# 1,2,5 & 10 are factors of 10, hence it is not a prime number.

# Constraints
# 1 <= n <= 10^9

# Topics
# Math





if __name__=='__main__':
    n=int(input())
    #Write your code here

    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print(str(n) + " is not a prime number")
                break
        else:
            print(str(n) + " is a prime number")
    else:
        print(str(n) + " is not a prime number")
