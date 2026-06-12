# https://leetcode.com/problems/solving-questions-with-brainpower/


# Recursion + Memoization

# TC: O(n) - Each state is computed once and there are O(n) states (index).
# SC: O(n) - The recursion stack can go as deep as O(n)
class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        n = len(questions)
        # DP array: sirf 1D array chahiye kyunki koi extra flag nahi hai
        dp = [-1] * n
        
        def solve(i):
            # Base Case: Agar hum array ke baahar nikal gaye, toh 0 points
            if i >= n:
                return 0
            
            # Memoization: Agar pehle se calculated hai, toh return kar do
            if dp[i] != -1:
                return dp[i]
            
            # Choice 1: Skip this question
            skip = solve(i + 1)
            
            # Choice 2: Solve this question
            points = questions[i][0]
            skip_count = questions[i][1]

            # Agla available index hoga: i + 1 + skip_count
            take = points + solve(i + 1 + skip_count)
            
            # Jo best ho use save kar lo
            dp[i] = max(skip, take)

            return dp[i]
            
        # 0th question se kahani shuru karo
        return solve(0)

print(Solution().mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]])) # 5


# Bottom-up DP

class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:

        n = len(questions)
        dp = [0] * (n + 1) # Extra space for base case

        # Bottom-up filling of DP array
        for i in range(n - 1, -1, -1):
            points = questions[i][0]
            skip_count = questions[i][1]

            # Choice 1: Skip this question
            skip = dp[i + 1]

            # Choice 2: Solve this question
            take = points + (dp[i + 1 + skip_count] if i + 1 + skip_count <= n else 0)

            dp[i] = max(skip, take)

        return dp[0]