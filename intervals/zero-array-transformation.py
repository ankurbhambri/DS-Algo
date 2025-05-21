# https://leetcode.com/problems/zero-array-transformation-i
#     
def isZeroArray(nums, queries):

    n = len(nums)
    diff = [0] * (n + 1)

    for l, r in queries:
        diff[l] += 1
        diff[r + 1] -= 1
    
    for i in range(1, n + 1):
        diff[i] += diff[i - 1]

    for n, q in zip(nums, diff):
        if n > q:
            return False
        
    return True


# https://leetcode.com/problems/zero-array-transformation-ii/

def minZeroArray(nums, queries):

    n = len(nums)
    left, right = 0, len(queries)

    def helper(k):

        n = len(nums)
        diff = [0] * (n + 1)

        for query_index in range(k):
            start, end, val = queries[query_index]
            diff[start] += val
            diff[end + 1] -= val

        for i in range(1, n + 1):
            diff[i] += diff[i - 1]

        for n, q in zip(nums, diff):
            if n > q:
                return False
        return True

    # Zero array isn't formed after all queries are processed
    if not helper(right):
        return -1                    

    # Binary Search
    while left <= right:
        m = left + (right - left) // 2
        if helper(m):
            right = m - 1
        else:
            left = m + 1
    return left
