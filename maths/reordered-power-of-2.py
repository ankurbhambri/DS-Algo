# https://leetcode.com/problems/reordered-power-of-2

from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        def count_digits(x):
            return Counter(str(x))
        
        n_count = count_digits(n)
        
        # check powers of 2 till 2^30 because 2^30 = 1073741824 > 1e9
        for i in range(31):

            if n_count == count_digits(1 << i):  # 1 << i = 2^i
                return True

        return False


print(Solution().reorderedPowerOf2(1))  # True
print(Solution().reorderedPowerOf2(10))  # False
print(Solution().reorderedPowerOf2(16))  # True
print(Solution().reorderedPowerOf2(24))  # False
print(Solution().reorderedPowerOf2(46))  # True
