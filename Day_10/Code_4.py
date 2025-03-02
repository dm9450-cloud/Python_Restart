# Fahrenheit to Celsius
# Given a temperature, of F in Fahrenheit, your task is to convert it into Celsius using the following equation:-

# T(°C) = (T(°F) - 32)*5/9

# Note: It is guaranteed that F - 32 will be a multiple of 9.

# Input Format
# The first line contains an integer that represents the Temperature in Fahrenheit.

# Output Format
# Return an integer containing the converted temperature in Celsius.

# Example 1
# Input

# 50
# Output

# 10
# Explanation

# (50-32) * 5/9 = 10

# Example 2
# Input

# -40
# Output

# -40
# Explanation

# (-40-32) * 5/9 = -40

# Constraints
# -1000 <= F <= 1000

# Topics
# Math

if __name__=='__main__':
    tempInFahr=int(input())
    # Write your code here and print the required output
    tempInCelsius= (tempInFahr-32)*5/9
    print(int(tempInCelsius))