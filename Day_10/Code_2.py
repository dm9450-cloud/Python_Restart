# Number of Days
# Given the number of the month, your task is to calculate the number of days present in the particular month.

# Note:- Consider non-leap year.

# Input Format
# An integer M, denoting the number of the month.

# Output Format
# Return the number of days in the month corresponding to the given number. Consider a non-leap year.

# Example 1
# Input

# 1
# Output

# 31
# Explanation

# January has 31 days.

# Example 2
# Input

# 3
# Output

# 31
# Explanation

# March has 31 days.

# Constraints
# 1 <= M <= 12

# Topics
# Conditionals


if __name__ == '__main__':
    month = int(input())
    # write code here
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        print("31")
    elif month==2:
        print("28")
    else:
        print("30")