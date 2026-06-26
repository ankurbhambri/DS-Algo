# https://leetcode.com/problems/parallel-courses-ii/

from itertools import combinations


class Solution:
    def minNumberOfSemesters(self, n: int, relations: list[list[int]], k: int) -> int:

        # Step 1: Har course ke prerequisites ko bitmask mein store karo
        # 0-indexed banane ke liye u-1 aur v-1 kar rahe hain
        prereq = [0] * n
        for u, v in relations:
            prereq[v - 1] |= (1 << (u - 1))

        # Total combinations 2^n hoti hain
        max_mask = 1 << n
        dp = [float('inf')] * max_mask
        dp[0] = 0 # Base case

        # Step 2: DP State transitions
        for mask in range(max_mask):

            if dp[mask] == float('inf'):
                continue

            # Abhi hum kaunse courses le sakte hain?
            available_courses = 0
            for i in range(n):
                # Agar course 'i' abhi tak nahi liya hai AND uske saare prereq completes hain
                if not (mask & (1 << i)) and (mask & prereq[i]) == prereq[i]:
                    available_courses |= (1 << i)

            # Available courses ke indices nikal lo
            choices = []
            for i in range(n):
                if available_courses & (1 << i):
                    choices.append(i)

            # Agar available courses 'k' se kam ya barabar hain, toh sabko le lo
            if len(choices) <= k:
                next_mask = mask | available_courses
                dp[next_mask] = min(dp[next_mask], dp[mask] + 1)
            else:
                # Agar 'k' se zyada hain, toh koi bhi 'k' courses chunno
                for combo in combinations(choices, k):
                    next_mask = mask
                    for course in combo:
                        next_mask |= (1 << course)
                    dp[next_mask] = min(dp[next_mask], dp[mask] + 1)

        return dp[max_mask - 1]


print(Solution().minNumberOfSemesters(4, [[2, 1], [3, 1], [1, 4]], 2))  # Output: 3
print(Solution().minNumberOfSemesters(5, [[2, 1], [3, 1], [4, 1], [1, 5]], 2))  # Output: 4