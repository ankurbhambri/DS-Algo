# https://leetcode.com/problems/palindrome-partitioning-iii/


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:

        n = len(s)

        # Step 1: Precompute min changes needed for any substring s[i...j]
        # cost[i][j] batayega s[i...j] ko palindrome banane ka kharcha
        cost = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):  # length 2 se n tak
            for i in range(n - length + 1):
                j = i + length - 1
                cost[i][j] = cost[i+1][j-1] + (0 if s[i] == s[j] else 1)

        # Step 2: DP function with Memoization
        memo = {}
        def solve(idx, partitions_left):

            # Base Case 1: Agar partitions khatam aur string bhi khatam -> Valid
            if idx == n and partitions_left == 0:
                return 0

            # Base Case 2: Agar string khatam par partition bache hain, ya vice versa -> Invalid
            if idx == n or partitions_left == 0:
                return float('inf')

            if (idx, partitions_left) in memo:
                return memo[(idx, partitions_left)]

            min_changes = float('inf')

            # i se lekar n tak har jagah cut maar ke dekho
            for next_idx in range(idx, n):
                current_cost = cost[idx][next_idx]
                remaining_cost = solve(next_idx + 1, partitions_left - 1)
                min_changes = min(min_changes, current_cost + remaining_cost)

            memo[(idx, partitions_left)] = min_changes
            return min_changes

        return solve(0, k)


print(Solution().palindromePartition("abc", 2))  # Output: 1
print(Solution().palindromePartition("aabbc", 3))  # Output: 0
print(Solution().palindromePartition("leetcode", 8))  # Output: 0