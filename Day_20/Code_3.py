# Palindrome Checker
# Given a number N, you need to check whether the given number is Palindrome or not. A number is said to be Palindrome when it reads the same from backwards as forward.

# Note: Input number will not have any trailing zeros.

# Input
# The line inputs N.

# Output
# You need to print "true" if the number is palindrome otherwise "false" (without quotes).

# Example 1
# Input

# 5
# Output

# true 
# Example 2
# Input

# 121
# Output

# true 
# Constraints:
# 1 <= N <= 9999

# Topics
# 2-Pointers
# Math
# Companies
# Samsung
# Oracle
# Adobe
# Zoho



class Solution:
    def solve(self, n):
    # Your code here  
        original_value=n
        rev_number=0
        while n>0:
            last_digit=n%10
            rev_number=rev_number*10+last_digit
            n//=10
        if original_value==rev_number:
            return "true"
        else:
            return "false"


def main():

    
    n = int(input())
    ob=Solution()
    ans=ob.solve(n)
    print(ans)

if __name__ == "__main__":
    main()
