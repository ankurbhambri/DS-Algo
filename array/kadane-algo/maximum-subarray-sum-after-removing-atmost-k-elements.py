# https://www.geeksforgeeks.org/maximum-subarray-sum-possible-after-removing-at-most-k-array-elements/

# Given an array arr[] of size N and an integer K, the task is to find the maximum subarray sum by removing at most K elements from the array.

# TC: O(n*k)
# SC: O(n*k)
def max_subarray_sum_after_k_removals(arr, k):

    n = len(arr)
    
    # Edge case: if k >= n, we can remove all negative elements
    if k >= n:
        return sum(max(0, x) for x in arr)
    
    # We'll use dynamic programming to solve this
    # dp[i][j] represents the maximum subarray sum ending at index i
    # after removing at most j elements
    dp = [[-float('inf')] * (k + 1) for _ in range(n)]
    
    # Base case: dp[0][0] = arr[0] (no removals)
    dp[0][0] = arr[0]
    
    # Base case: dp[0][1] = 0 (remove the first element if negative)
    dp[0][1] = 0 if k > 0 else -float('inf')

    for i in range(1, n):
        for j in range(k + 1):

            # Option 1: Include the current element in the subarray
            include = max(dp[i-1][j] + arr[i], arr[i])
            
            # Option 2: Remove the current element (if j > 0)
            exclude = dp[i-1][j-1] if j > 0 else -float('inf')
            
            dp[i][j] = max(include, exclude)
    
    return max(dp[n-1])

# Test cases
test_cases = [
    ([(-2), 1, 3, (-2), 4, (-7), 20], 1),
    ([(-1), 1, (-1), (-1), 1, 1], 2),
]

for i, (arr, k) in enumerate(test_cases):
    result = max_subarray_sum_after_k_removals(arr, k)
    print(f"Test case {i+1}: {result}")
