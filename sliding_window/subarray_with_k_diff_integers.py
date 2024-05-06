# https://leetcode.com/problems/subarrays-with-k-different-integers/


def subarraysWithKDistinct(nums, k):
    freq = {}

    l, r = 0, 0

    res = 0

    for n in nums:

        freq[n] = freq.get(n, 0) + 1

        if len(freq) > k:
            # remove distinct value from r index and increment r, l
            del freq[nums[r]]

            r += 1

            l = r

        if len(freq) == k:
            # update r and res (Notice: K >= 1)
            while freq[nums[r]] > 1:
                freq[nums[r]] -= 1

                r += 1

            # size of window
            res += r - l + 1

    return res


print(subarraysWithKDistinct(nums=[1, 2, 1, 2, 3], k=2))
