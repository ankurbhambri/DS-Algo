# https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/


class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, r: int) -> str:

        st = []
        n_letters = len([c for c in s if c == letter])

        for i, c in enumerate(s):

            remaining_chars = len(s) - i

            while st and st[-1] > c and (remaining_chars + len(st) > k) and (st[-1] != letter or n_letters > r):
                d = st.pop()
                if d == letter:
                    r += 1

            if len(st) < k:

                if c == letter:
                    st.append(c)
                    r -= 1

                elif k - len(st) > r:
                    st.append(c)

            if c == letter:
                n_letters -= 1

        return ''.join(st)


print(Solution().smallestSubsequence("leet", 3, "e", 1))          # "eet"
print(Solution().smallestSubsequence("leetcode", 4, "e", 2))      # "ecde"
print(Solution().smallestSubsequence("bb", 2, "b", 2))            # "bb"
print(Solution().smallestSubsequence("abcde", 5, "a", 1))          # "abcde"
