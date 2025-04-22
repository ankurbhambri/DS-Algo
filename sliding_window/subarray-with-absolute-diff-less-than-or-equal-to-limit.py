# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/

from collections import deque

def longestSubarray( nums, limit: int) -> int:

    l = 0

    min_q = deque()
    max_q = deque()

    n = len(nums)
    res = 0

    for r in range(n):

        while min_q and nums[min_q[-1]] > nums[r]:
            min_q.pop()

        while max_q and nums[max_q[-1]] < nums[r]:
            max_q.pop()

        min_q.append(r)
        max_q.append(r)

        while min_q and max_q and nums[max_q[0]] - nums[min_q[0]] > limit:

            if min_q and nums[min_q[0]] == nums[l]:
                min_q.popleft()

            if max_q and nums[max_q[0]] == nums[l]:
                max_q.popleft()

            l += 1

        res = max(res, r - l + 1)

    return res


print(longestSubarray([8,2,4,7], 4))
print(longestSubarray([10,1,2,4,7,2], 5))
print(longestSubarray([4,2,2,2,4,4,2,2], 0))
print(longestSubarray([1,3,6,7,8,9], 4))
