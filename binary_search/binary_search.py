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
def lowerbound(target, nums):

    l, r = 0, len(nums) - 1

    while l < r:

        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        else:
            r = m - 1

    return l


def upperbound(target, nums):

    l, r = 0, len(nums) - 1

    while l < r:

        m = (l + r) // 2
        if nums[m] <= target:
            l = m + 1
        else:
            r = m - 1

    return r


print("lowerbound ", lowerbound(2, [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8]))
print("upperbound ", upperbound(2, [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8]))

print("lowerbound ", lowerbound(9, [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8, 9, 10, 10]))
print("upperbound ", upperbound(9, [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 8, 9, 10, 10]))


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
