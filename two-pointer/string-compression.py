# https://leetcode.com/problems/string-compression/description/


class Solution:
    def compress(self, chars: list[str]) -> int:

        i = 0
        write = 0

        n = len(chars)

        while i < n:

            ch = chars[i]
            count = 0

            # count same chars
            while i < n and chars[i] == ch:
                i += 1
                count += 1

            # write character
            chars[write] = ch
            write += 1

            # write frequency if > 1
            if count > 1:

                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write


print(Solution().compress(["a", "a", "b", "b", "c", "c", "c"]))
print(Solution().compress(["a", "a", "b", "b", "b", "b", "b", "b", "b", "b", "c", "z", "c", "c", "c", "x", "y", "x", "y","y"]))

'''
    The function returns `write`, which represents the length of the compressed string.
    For example, given the input ["a", "a", "b", "b", "b", "b", "b", "b", "b", "b", "c", "z", "c", "c", "c", "x", "y", "x", "y", "y"],
    the compressed version of the string up to index `write` would be:
    ["a", "2", "b", "8", "c", "z", "c", "3", "x", "y", "x", "y", "2"].
    The remaining elements beyond index `write` are irrelevant for the compressed result.
'''