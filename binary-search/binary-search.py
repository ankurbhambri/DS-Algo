"""
Binary Search Variants:

1. Search for a specific value:
    - Range: [0, len(arr) - 1]
    - Loop condition: while l <= r
    - Use when searching for an exact match.

2. Lower or Upper Bound:
    - Range: [0, len(arr)]
    - Loop condition: while l < r
    - Best choice for finding boundaries (e.g., lower or upper bound).
"""

def binary_search(target, nums):

    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2  # l + (r - l) // 2 (to avoid overflow)
        if target == nums[m]:
            return m
        elif target > nums[m]:
            l = m + 1
        else:
            r = m - 1

    return -1


print(binary_search(2, [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8]))
print(binary_search(2, [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8, 9, 10, 10]))


# If we have to get lower bound element index
def lowerbound(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid
    return left

a = lowerbound([1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8], 2) # first index of an element.
b = upper_bound([1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8], 2) # last index of an element.

print("Range of 2: ", b - a)

print("lowerbound of 2: ", lowerbound([1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8], 2))
print("upperbound  of 2: ", upper_bound([1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8], 2))


# genric function for lower and upper bound
def genric_bound(arr, x, compare_logic):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if compare_logic(arr[mid], x):
            left = mid + 1
        else:
            right = mid
    return left


# lower bound - lambda a, b: a < b
# upper bound - lambda a, b: a <= b

print(genric_bound([1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8], 2, lambda a, b: a < b))
print(genric_bound([1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8, 9, 10, 10], 2, lambda a, b: a <= b))

# we can also count nos of elemet in array like in this 2's are 4 times in nums
nums = [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8]
print(genric_bound(nums, 2, lambda a, b: a <= b) - genric_bound(nums, 2, lambda a, b: a < b))

nums = [5,7,7,8,8,10]
print(genric_bound(nums, 8, lambda a, b: a < b), genric_bound(nums, 8, lambda a, b: a <= b))
