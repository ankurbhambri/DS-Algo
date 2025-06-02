"""
    https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

    Given a string S, find the length of the longest substring T that contains at most k distinct characters.

    Note - same as above replace static value 2 with k only

    Similar question - https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/ replace k with 2

"""


class Solution:
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:

        if k == 0:
            return 0

        if k > len(s):
            return len(s)

        l = 0
        hm = {}
        res = 0

        for r in range(len(s)):

            hm[s[r]] = 1 + hm.get(s[r], 0)

            if len(hm) > k:

                hm[s[l]] -= 1
                if hm[s[l]] == 0:
                    del hm[s[l]]
                l += 1

            res = max(res, r - l + 1)

        return res


obj = Solution()
print(obj.length_of_longest_substring_k_distinct("eceba", 2))  # 3
print(obj.length_of_longest_substring_k_distinct("aa", 1))  # 2
print(
    obj.length_of_longest_substring_k_distinct(
        "nfhiexxjrtvpfhkrxcutexxcodfioburrtjefrgwrnqtyzelvtpvwdvvpsbudwtiryqzzy", 25
    )
)  # 70
