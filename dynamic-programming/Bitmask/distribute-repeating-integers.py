# https://leetcode.com/problems/distribute-repeating-integers


# https://cp-algorithms.com/algebra/all-submasks.html

from collections import Counter

# TC: O(2^m * n) where m is the number of customers and n is the number of unique integers in nums
# SC: O(2^m) for the memoization dictionary and total_quantity array
class Solution:
    def canDistribute(self, nums: list[int], quantity: list[int]) -> bool:

        # Step 1: Frequencies nikalna
        counts = list(Counter(nums).values())

        m = len(quantity)

        # Precompute: Har ek mask ke liye total kitni quantity chahiye
        # Taaki baar-baar loop chala kar sum na nikalna pade

        total_quantity = [0] * (1 << m)
        for mask in range(1 << m):
            current_sum = 0
            for i in range(m):
                if mask & (1 << i):  # Agar ith customer is mask mein shamil hai
                    current_sum += quantity[i]
            total_quantity[mask] = current_sum

        memo = {}

        # Step 2: DP Function
        def solve(i, mask):

            # Base Case 1: Agar saare customers khush ho gaye (Mask ke saare bits 1 ho gaye)
            if mask == (1 << m) - 1:
                return True

            # Base Case 2: Agar counts array khatam ho gaya par customers baaki hain
            if i >= len(counts):
                return False

            state = (i, mask)
            if state in memo:
                return memo[state]

            # Choice 1: Is current frequency (counts[i]) se kisi customer ko kuch mat do
            # Direct agale number ki frequency par chale jao
            if solve(i + 1, mask):
                memo[state] = True
                return True

            # Choice 2: Jo customers abhi baaki hain, unke submasks nikalte hain
            # Jo customers bache hain unka mask hoga: (~mask) aur unhe limit karenge available bits tak
            remaining_customers = ((1 << m) - 1) ^ mask

            submask = remaining_customers

            while submask > 0:

                # Agar is submask wale customers ki total demand hamare paas available count se kam ya barabar hai
                if total_quantity[submask] <= counts[i]:

                    # Toh unhe yeh de do, aur mask mein unhe shamil kar lo (mask | submask)
                    if solve(i + 1, mask | submask):
                        memo[state] = True
                        return True

                # Agla submask dhoondo (Bitwise Magic)
                submask = (submask - 1) & remaining_customers

            memo[state] = False
            return False

        return solve(0, 0)


# print(Solution().canDistribute([1, 2, 3], [2]))  # True
# print(Solution().canDistribute([1, 2, 3, 4], [2]))  # False
# print(Solution().canDistribute([1, 2, 3, 4, 5], [2, 1]))  # True
print(Solution().canDistribute([1, 2, 3, 4, 5], [2, 2]))  # False