# Conditional Problem 6
# You are given two integers a and b. You need to perform the following operations

# If both integers are odd, print `we are odd`.
# Else print `we are simple`.
# Input Format
# First line contains two variables a and b.

# Output Format
# Output will be "we are odd" if both the variables are odd numbers. Otherwise output will be "we are simple".

# Example 1
# Input

# 1 3
# Output

# we are odd
# Example 2
# Input

# 2 5
# Output

# we are simple
# Constraints
# -10^8 <= a, b <= 10^8

# Topics
# Conditionals


if __name__=='__main__':
    n,m = map(int,input().split())
    # write code here

if n%2!=0 and m%2!=0:
    print("we are odd")
else:
    print("we are simple")