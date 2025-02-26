# Mathematical Operations
# You are given two positive integers. You have to calculate the result by performing +,-,*,/,% operations on them.

# Input Format
# The first line of input contains two space-separated integers A and B.

# Output Format
# The first line of the output should contain the sum of A and B.

# The second line of the output should contain the difference of A and B.

# The third line of the output should contain the product of A and B.

# The fourth line of the output should contain the quotient of A divided by B.

# The fifth line of the output should contain the remainder of A modulus by B.

# Example 1
# Input:

# 8 3
# Output:

# 11
# 5
# 24
# 2
# 2
# Example 2
# Input:

# 10 2
# Output:

# 12
# 8
# 20
# 5
# 0
# Constraints
# 1 <= A <= 10^3

# 1 <= B <= 10^3

# Topics
# Math
# Companies
# Walmart Global Tech




if __name__ == '__main__':
    (a, b) = list(map(int, input().split()))
     #Write your code here
     #Print output 
    add = a+b
    diff = a-b
    product = a*b
    division = a/b
    mod = a%b

    print(int(add))
    print(int(diff))
    print(int(product))
    print(int(division))
    print(int(mod))
