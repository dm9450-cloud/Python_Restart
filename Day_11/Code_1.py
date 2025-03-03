# Quadrants
# Four friends are in a mystery room and they aim to get out of the mystery room by cracking the final trail. The mystery room is divided into four chambers and each chamber will have two boxes storing balls. Now if both the boxes have blue balls, it must belong to chamber 1. Similarly if the first box has red balls and second box has blue balls, they must belong to chamber 2. If both the boxes have red balls, they must belong to chamber 3. Finally if the first box has blue balls and second box has red balls, it must belong to chamber 4.

# You are given number of balls in each box and if the number has a negative sign it means the balls are red else the balls are blue if the sign is positive. Determine the chamber the two boxes belong to given the number and type of balls in each box.

# Note: Assume there will always be non-zero number of balls in each box.

# Input
# The input consists of two lines.

# The first line of input denotes the number and type of balls in the first box.

# The second line of input denotes the number and type of balls in the second box.

# Output
# Output the chamber number (1, 2, 3 or 4) for the given count of balls in each box.

# Example 1
# Input

# 10
# 6
# Output

# 1
# Explanation: The first box has 10 blue balls and the second box has 6 blue balls hence it belongs to chamber 1.

# Example 2
# Input

# 9
# -13
# Output

# 4
# Explanation: The first box has 9 blue balls and the second box has 13 red balls hence it belongs to chamber 4.

# Constraints
# -109 <= x,y <= 109

# Topics
# Math


if __name__=='__main__':
    x = int(input())
    y = int(input())
    #Write your code here
    if x > 0 and y > 0:
        print(1)
    elif x < 0 and y > 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    else:
        print(4)
        