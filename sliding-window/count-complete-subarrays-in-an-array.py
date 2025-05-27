def countCompleteSubarrays(nums):

    l = 0
    res = 0
    freq = {} 

    n = len(nums)
    k = len(set(nums))

    for r in range(n):
        freq[nums[r]] = 1 + freq.get(nums[r], 0)

        while len(freq) == k:
            res += (n - r)
            freq[nums[l]] -= 1
            if freq[nums[l]] == 0:
                del freq[nums[l]]
            l += 1

    return res

print(countCompleteSubarrays([1,3,1,2,2]))  # Output: 4
print(countCompleteSubarrays([5,5,5,5]))  # Output: 10


# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description

def countSubarrays(nums, k):

    l = 0
    res = 0
    freq = {}
    n = len(nums)
    max_ele = max(nums)

    for i in range(len(nums)):

        freq[nums[i]] = 1 + freq.get(nums[i], 0)

        while max_ele in freq and freq[max_ele] >= k:

            res += n - i
            freq[nums[l]] -= 1

            if freq[nums[l]] == 0:
                del freq[nums[l]]

            l += 1

    return res

print(countSubarrays([1,3,2,3,3], 2))  # Output: 6
print(countSubarrays([1,4,2,1], 3))  # Output: 0
