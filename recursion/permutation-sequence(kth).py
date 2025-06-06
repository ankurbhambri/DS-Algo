# https://leetcode.com/problems/permutation-sequence/description/

'''

Initialize list of numbers → nums = [1, 2, ..., n]

Convert k to 0-based index → k = k - 1

For each position (from n to 1):

    Calculate (i-1)!

    Find index = k // (i-1)! → this tells which number to pick

    Add nums[index] to result

    Remove that number from nums

    Update k = k % (i-1)!

    Join result list into string and return

'''

import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        # this is required to get the value from that index
        nums = [str(i) for i in range(1, n + 1)]
        k -= 1  # Convert to 0-based index
        result = []

        for i in range(n, 0, -1):
            fact = math.factorial(i - 1) # like n == 4 then take 4 - 1  = 3! = 6

            index = k // fact # 9 // 4 = 1, select this index from nums

            result.append(nums.pop(index)) # Append the selected number to the result

            k %= fact

        return ''.join(result)
    
print(Solution().getPermutation(3, 3))  # "213"
print(Solution().getPermutation(4, 9))  # "2314"
