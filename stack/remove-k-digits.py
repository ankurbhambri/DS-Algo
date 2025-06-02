# https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for digit in num:

            while st and k > 0 and st[-1] > digit:
                st.pop()
                k -= 1
            st.append(digit)
        
        # Remove remaining digits from the end if k > 0
        final_stack = st[:-k] if k else st
        
        # Strip leading zeros
        result = ''.join(final_stack).lstrip('0')
        
        return result if result else "0"

print(Solution().removeKdigits("1432219", 3))  # Output: "1219"
print(Solution().removeKdigits("10200", 1))    # Output: "200"
print(Solution().removeKdigits("10", 2))        # Output: "0"
print(Solution().removeKdigits("9", 1))         # Output: "0"