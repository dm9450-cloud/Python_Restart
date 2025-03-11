# Print Even Numbers
# You are given an integer N. Your task to print all the even numbers from 0 to N.

# Input Format
# The input contains a single integer N.

# Output Format
# Output all the even numbers from 0 to N.

# Example 1
# Input:

# 8
# Output:

# 0 2 4 6 8
# Example 2
# Input:

# 7
# Output:

# 0 2 4 6



class Solution:    
    def evenNumber(self,n):
        #Write your code here and print output here
        # i=0
        # while i<=n:
        #     if(i%2==0):
        #         print(i,end=" ")
        #     i+=1
        for i in range(0,n+1):
            if(i%2==0):
                print(i,end=" ")
                i+=1
if __name__=='__main__':
    n = int(input())
    Obj = Solution()
    Obj.evenNumber(n)