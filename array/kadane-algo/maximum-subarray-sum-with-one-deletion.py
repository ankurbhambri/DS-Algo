# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/description/

# TC: O(n)
# SC: O(1)
def maximumSum(arr):

    n = len(arr)
    if n == 0:
        return 0

    no_del = arr[0]
    one_del = arr[0]
    res = arr[0]

    for i in range(1, n):
        one_del = max(no_del, one_del + arr[i])
        no_del = max(arr[i], no_del + arr[i])
        res = max(res, no_del, one_del)

    return res


print(maximumSum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 10
print(maximumSum([1, -2, 0, 3]))  # Output: 4
print(maximumSum([-1, -1, -1, -1]))  # Output: -1
print(maximumSum([5, 4, -1, 7, 8]))  # Output: 24
print(maximumSum([1, 2, 3, -2, 5]))  # Output: 11
