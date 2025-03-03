# Conditional Problem 2
# You are given a number N. Write a program using If Else such that if N is less than 30 then the output will be "less important" otherwise the output will be "more important".

# Input Format
# The first line contains an integer.

# Output Format
# If the number is less than 30 then "less important" will be printed. If the number is not less than 30 then "more important" will be printed.

# Example 1
# Input

# 30
# Output

# more important
# Explanation

# Since 30 is not less than 30 answer is "more important".

# Example 2
# Input

# 23
# Output

# less important
# Explanation

# Since 23 is less than 30 answer is "less important".

# Constraints:
# 1 <= N <= 10^5
# Topics
# Conditionals

if __name__ == '__main__':
    n = int(input())
    # write code here
    if(n<30):
        print("less important")
    else:
        print("more important")
        