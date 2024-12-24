# https://leetcode.com/problems/sum-of-subarray-ranges/description/


def subArrayRanges(nums):

    n, answer = len(nums), 0
    stack = []

    # Find the sum of all the minimum.
    for right in range(n + 1):
        while stack and (right == n or nums[stack[-1]] >= nums[right]):
            mid = stack.pop()
            left = -1 if not stack else stack[-1]
            answer -= nums[mid] * (mid - left) * (right - mid)
        stack.append(right)

    # Find the sum of all the maximum.
    stack = []
    for right in range(n + 1):
        while stack and (right == n or nums[stack[-1]] <= nums[right]):
            mid = stack.pop()
            left = -1 if not stack else stack[-1]
            answer += nums[mid] * (mid - left) * (right - mid)
        stack.append(right)

    return answer


print(subArrayRanges([1, 2, 3]))  # Output: 4
print(subArrayRanges([1, 3, 3]))  # Output: 4
print(subArrayRanges([4, -2, -3, 4, 1]))  # Output: 59
print(subArrayRanges([5, 4, 3, 2, 1]))  # Output: 20
print(subArrayRanges([5, 6, 7, 8, 1, 2]))  # Output: 67
