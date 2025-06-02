# https://leetcode.com/problems/string-compression/description/

class Solution:
    def compress(self, chars):

        l, r = 0, 0

        while r < len(chars):

            chars[l] = chars[r]
            count = 1

            while r + 1 < len(chars) and chars[r] == chars[r+1]:
                r += 1
                count += 1

            if count > 1:
                for c in str(count):
                    chars[l + 1] = c
                    l += 1

            r += 1
            l += 1

        return l

print(Solution().compress(["a", "a", "b", "b", "b", "b", "b", "b", "b", "b", "c", "z", "c", "c", "c", "x", "y", "x", "y","y"]))
'''

- The function returns `l`, which represents the length of the compressed string.
- For example, given the input ["a", "a", "b", "b", "b", "b", "b", "b", "b", "b", "c", "z", "c", "c", "c", "x", "y", "x", "y", "y"],
- the compressed version of the string up to index `l` would be:
- ["a", "2", "b", "8", "c", "z", "c", "3", "x", "y", "x", "y", "2"].
- The remaining elements beyond index `l` are irrelevant for the compressed result.

'''