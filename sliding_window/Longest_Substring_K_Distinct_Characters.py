# https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/


class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

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


# Test Cases
obj = Solution()
print(obj.length_of_longest_substring_k_distinct("eceba", 2))  # 3
print(obj.length_of_longest_substring_k_distinct("aa", 1))  # 2
print(
    obj.length_of_longest_substring_k_distinct(
        "nfhiexxjrtvpfhkrxcutexxcodfioburrtjefrgwrnqtyzelvtpvwdvvpsbudwtiryqzzy", 25
    )
)  # 70
