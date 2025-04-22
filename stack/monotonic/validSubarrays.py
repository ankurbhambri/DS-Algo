'''

Q) Given an array A of integers, return the number of non-empty continuous subarrays that satisfy the following condition:

The leftmost element of the subarray is not larger than other elements in the subarray.


Example 1:

    Input: [1,4,2,5,3]
    Output: 11
    Explanation: There are 11 valid subarrays: [1],[4],[2],[5],[3],[1,4],[2,5],[1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3].
    Example 2:

    Input: [3,2,1]
    Output: 3
    Explanation: The 3 valid subarrays are: [3],[2],[1].
    Example 3:

    Input: [2,2,2]
    Output: 6
    Explanation: There are 6 valid subarrays: [2],[2],[2],[2,2],[2,2],[2,2,2].

Note:

    1 <= A.length <= 50000
    0 <= A[i] <= 100000

'''

# O(N^2)
def solution(A):
    res = len(A)
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] > A[j]:
                break
            res += 1
    return res

print(solution([1, 4, 2, 5, 3]))
print(solution([3, 2, 1]))
print(solution([2, 2, 2]))


# O(N)
def validSubarrays(A):
    n = len(A)
    stack = []
    total = 0
    
    # Iterate through each index
    for i in range(n):
        # Pop elements from stack while stack is not empty and current element is smaller
        while stack and A[i] < A[stack[-1]]:
            # Pop the index from stack
            j = stack.pop()
            # The number of subarrays starting at index j is (i - j)
            # Because subarrays are from j to j, j to j+1, ..., j to i-1
            total += i - j
        # Push current index onto stack
        stack.append(i)
    
    # Process remaining indices in stack
    while stack:
        j = stack.pop()
        # For these indices, valid subarrays extend to the end of array
        total += n - j
    
    return total

print(validSubarrays([1, 4, 2, 5, 3]))
print(validSubarrays([3, 2, 1]))
print(validSubarrays([2, 2, 2]))
print(validSubarrays([0, 1, 0, 1, 0, 1]))
