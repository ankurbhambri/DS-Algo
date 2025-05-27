# https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        
        seen = set()
        swaps = 0
        
        for i in range(len(s1)):

            if s1[i] != s2[i]:

                seq = s1[i] + s2[i]
                
                if seq in seen:

                    seen.remove(seq)
                    swaps += 1

                else:
                    seen.add(seq)
                    
        if len(seen) == 1:
            return -1

        if len(seen) == 2:
            return swaps + 2

        return swaps

print(Solution().minimumSwap("xx", "yy"))  # Output: 1
print(Solution().minimumSwap("xy", "yx"))  # Output: 2
print(Solution().minimumSwap("xxyyxyxyxx", "xyyxyxxxyx"))  # Output: 4
print(Solution().minimumSwap("xxyyxyxyxx", "xyyxyxxxyy"))  # Output: -1