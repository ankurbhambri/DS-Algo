# https://leetcode.com/problems/maximum-swap/

class Solution:
    def maximumSwap(self, num: int) -> int:

        # Number ko list mein badle taaki swap kar sakein
        s = list(str(num))

        # Step 1: Har digit ki last position store karein
        last = {int(digit): i for i, digit in enumerate(s)}

        # Step 2: Left side se scan karein
        for i, digit in enumerate(s):
            # Step 3: Check karein kya koi bada digit (9 down to current) baad mein hai?
            for d in range(9, int(digit), -1):
                if last.get(d, -1) > i:
                    # Step 4: Swap karein aur return kar dein
                    s[i], s[last[d]] = s[last[d]], s[i]
                    return int("".join(s))  
        return num

print(Solution().maximumSwap(2736))  # Output: 7236
print(Solution().maximumSwap(9973))  # Output: 9973

# Note: After this please revise the next-permutation.py file