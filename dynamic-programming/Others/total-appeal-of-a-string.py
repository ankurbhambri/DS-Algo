# https://leetcode.com/problems/total-appeal-of-a-string

# similar to https://leetcode.com/discuss/post/1481915/amazon-oa-count-distinct-characters-in-a-gr6u/


# TC: O(n)
# SC: O(n)
class Solution:
    def appealSum(self, s: str) -> int:

        n = len(s)
        ans = 0
        last_seen = {}

        for i, char in enumerate(s):

            # Pichli baar yeh character kahan dikha tha (Nahi dikha toh -1)
            prev_idx = last_seen.get(char, -1)

            # Formula: left choices * right choices
            left = i - prev_idx  # Left choices
            right = n - i       # Right choices

            ans += left * right

            # Current index ko update kar do
            last_seen[char] = i

        return ans


print(Solution().appealSum("code")) # 20
print(Solution().appealSum("abbca")) # 28