def solution(A):
    odd_count=sum(1 for num in A if num%2!=0)
    even_count = len(A)-odd_count
    return min(odd_count,even_count)>=(len(A)//2)

# A=[2,7,4,6,3,1]
# A=[-1,1]
# A=[2,-1]
A=[1,2,4,3]
print(solution(A))
