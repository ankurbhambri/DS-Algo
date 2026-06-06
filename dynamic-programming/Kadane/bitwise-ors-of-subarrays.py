# https://leetcode.com/problems/bitwise-ors-of-subarrays/


# TC: O(n^2) in worst case, but usually much better due to the nature of bitwise OR
# SC: O(n) for the sets used to store unique ORs
class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:

        ans = set()       # Saare unique results store karne ke liye
        current_or = set() # Pichle step ke unique ORs ke liye

        for x in arr:

            # Pichle saare ORs ka x ke saath bitwise OR nikalo, aur x ko bhi shamil karo
            current_or = {num | x for num in current_or} | {x}

            # Is step ke results ko final ans set mein update kar do
            ans.update(current_or)

        return len(ans)


print(Solution().subarrayBitwiseORs([0]))  # Output: 1
print(Solution().subarrayBitwiseORs([1, 1, 2]))  # Output: 3