# https://leetcode.com/problems/kth-missing-positive-number/

"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
Return the kth positive integer that is missing from this array.
"""

# TC: O(log N)
# SC: O(1)
def findKthPositive(arr, k):

    l, r = 0, len(arr)

    while l < r:

        m = (l + r) // 2

        # How many missing see the index and do index + 1 and minus with present number arr[m] - (m + 1) # of missing number
        # Becasue at index 0 the number should be 1, at index 1 the number should be 2, at index 2 the number should be 3 and so on.
        # So in case at index 3 the number is 5, so how many missing number till index 3 is arr[3] - (3 + 1) = 5 - 4 = 1 missing number.
        if arr[m] - (m + 1) < k:
            l = m + 1

        else:
            r = m

    return l + k # found the index till this point how many missing k numbers, add it.


print(findKthPositive([1, 2, 3, 4], 2))  # 6
print(findKthPositive([2, 3, 4, 7, 11], 5))  # 9


# Variant: Kth missing number starting from the leftmost number of the array.

def findKthPositiveVariant(arr, k):

    if not arr:
        return k

    l, r = 0, len(arr)
    start_val = arr[0]

    while l < r:
        m = (l + r) // 2

        # Missing numbers starting from arr[0]
        # Formula: (Current Value - Start Value) - (Number of elements in between)
        missing_count = (arr[m] - start_val) - m

        if missing_count < k:
            l = m + 1
        else:
            r = m

    # Logic for return:
    # l-1 is the last index where missing < k
    # Result = arr[l-1] + (k - missing_till_l-1)
    # Simplified: return start_val + l + k - 1
    return start_val + l + k - 1


print(findKthPositiveVariant([], 4))  # 4
print(findKthPositiveVariant([5, 6, 7, 8, 9], 3))  # 7
print(findKthPositiveVariant([2, 3, 4, 7, 11], 5))  # 10