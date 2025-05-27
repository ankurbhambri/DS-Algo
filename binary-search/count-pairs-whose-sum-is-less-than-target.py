# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

def countPairs(nums, target):

    res = 0
    nums.sort()
    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l] + nums[r] < target:
            res += r - l
            l += 1
        else:
            r -= 1

    return res

print(countPairs([1, 2, 3, 4], 5)) # Output: 4
print(countPairs([1, 2, 3, 4], 10))
print(countPairs([1, 2, 3, 4], 0))
print(countPairs([1, 2, 3, 4], 1))
