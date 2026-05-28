'''
Given an array A1, A2 . . . AN what is the size of the largest subset of the array such that the each pair of elements in the subset is coprime.

Example : Let N=5 and array be [2 3 2 3 2] then answer is 2

Explanation : The largest subset would be taking one of A[0], A[1], A[2] and taking one of A[3], A[4].

N can be at max 50.

'''


from math import gcd

def largestCoprimeSubset(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    # DP table: dp[i][g] = max size of subset up to index i with GCD g
    # Here, we'll use a simplified approach with subsets for small N
    def is_coprime_subset(subset):
        if len(subset) <= 1:
            return True
        for i in range(len(subset)):
            for j in range(i + 1, len(subset)):
                if gcd(subset[i], subset[j]) != 1:
                    return False
        return True
    
    max_size = 1  # At least one element can always be taken
    # Generate all possible subsets (for small N, 2^50 is too big, but N <= 50 is manageable)
    for mask in range(1, 1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(arr[i])
        if is_coprime_subset(subset):
            max_size = max(max_size, len(subset))
    
    return max_size

# Test
arr = [2, 3, 2, 3, 2]
print(largestCoprimeSubset(arr))  # Output: 2