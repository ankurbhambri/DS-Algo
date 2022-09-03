def binary_search(x, nums):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if x == nums[m]:
            return m
        elif x > nums[m]:
            l = m + 1
        else:
            r = m - 1
    return -1


# will return 2 different index based on element shifiting
print(binary_search(2, [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8]))
# issue with classic binary serach is it change index with element shifting
print(binary_search(2, [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8, 9, 10, 10]))


# If i have to to get lower bound element index
def lowerbound(x, nums):
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if x <= nums[m]:
            r = m
        else:
            l = m + 1
    return l


# This will return lower index for element 2 in both cases
print(lowerbound(2, [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8]))
print(lowerbound(2, [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8, 9, 10, 10]))


# If i have to to get upper bound element index
def upperbound(x, nums):
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if x < nums[m]:
            r = m
        else:
            l = m + 1
    return l


# This will return uper bound index for element 2 in both cases but 1 father than actual index
print(upperbound(2, [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8]))
print(upperbound(2, [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8, 9, 10, 10]))


# genric function for lower and upper bound
def genric_bound(x, nums, compare):
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if compare(x, nums[m]):
            r = m
        else:
            l = m + 1
    return l


lower = lambda x, elem: x <= elem
upper = lambda x, elem: x < elem
print(genric_bound(2, [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8], lower))
print(genric_bound(2, [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8, 9, 10, 10], upper))


# we can also count nos of elemet in array like in this 2's are 4 times in nums
nums = [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8]
print(genric_bound(2, nums, upper) - genric_bound(2, nums, lower))
