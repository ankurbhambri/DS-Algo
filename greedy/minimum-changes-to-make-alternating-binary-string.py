# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/


class Solution:
    def minOperations(self, s: str) -> int:

        flips_a = 0  # '0101...' pattern
        flips_b = 0  # '1010...' pattern

        for i, char in enumerate(s):
            expected_a = '0' if i % 2 == 0 else '1'
            expected_b = '1' if i % 2 == 0 else '0'

            if char != expected_a:
                flips_a += 1
            if char != expected_b:
                flips_b += 1

        return min(flips_a, flips_b)
    
print(Solution().minOperations("0100"))  # Output: 1
print(Solution().minOperations("10"))    # Output: 0