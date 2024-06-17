def binary_search(target, nums):
    l, r = 0, len(nums) - 1
    while l <= r:
        # l + (r - l) // 2 (to avoid overflow)
        m = (l + r) // 2
        if target == nums[m]:
            return m
        elif target > nums[m]:
            l = m + 1
        else:
            r = m - 1
    return -1


# will return 2 different index based on element shifiting
print(binary_search(2, [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8]))

# issue with classic binary serach that, it changes the index with element shifting
print(binary_search(2, [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8, 9, 10, 10]))


# If we have to get lower bound element index
def lowerbound(target, nums):
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if target <= nums[m]:
            r = m
        else:
            l = m + 1
    return l


# This will return lower index for element 2 in both cases
print(lowerbound(9, [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8]))
print(lowerbound(2, [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8, 9, 10, 10]))


# If we have to get upper bound element index
def upperbound(target, nums):
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if target < nums[m]:
            r = m
        else:
            l = m + 1
    return l


# This will return uper bound index for element 2 in both cases but 1 father than actual index
print(upperbound(2, [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8]))
print(upperbound(2, [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8, 9, 10, 10]))


# genric function for lower and upper bound
def genric_bound(target, nums, compare):
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if compare(target, nums[m]):
            r = m
        else:
            l = m + 1
    return l


lower = lambda target, elem: target <= elem
upper = lambda target, elem: target < elem
print(genric_bound(2, [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8], lower))
print(genric_bound(2, [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8, 9, 10, 10], upper))


# we can also count nos of elemet in array like in this 2's are 4 times in nums
nums = [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8]
print(genric_bound(2, nums, upper) - genric_bound(2, nums, lower))
