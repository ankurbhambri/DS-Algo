# https://leetcode.com/problems/best-team-with-no-conflicts/


# TC: O(n^2)
# SC: O(n)
class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:

        # Step 1: Age aur Score ko pair up karke sort karo
        # Pehle age se sort hoga, agar age same hai toh score se sort hoga
        players = sorted(zip(ages, scores))

        n = len(players)
        # dp[i] store karega maximum score jo hum player 'i' ko include karke bana sakte hain
        dp = [0] * n

        # Har player ke liye check karenge
        for i in range(n):

            current_score = players[i][1]
            dp[i] = current_score  # Base case: Akela yeh player team mein ho

            # Isse pehle wale saare players ko check karo
            for j in range(i):
                prev_score = players[j][1]

                # Sorterd hone ki wajah se players[i] ki age >= players[j] ki age toh hai hi.
                # Conflict tabhi nahi hoga agar current player ka score pichle player se bada ya barabar ho.
                if current_score >= prev_score:
                    dp[i] = max(dp[i], dp[j] + current_score)

        # Jo bhi maximum score mila, woh hamara answer hai
        return max(dp)


print(Solution().bestTeamScore(scores=[4, 5, 6, 5], ages=[2, 1, 2, 1]))  # Output: 16
print(Solution().bestTeamScore(scores=[1, 3, 5, 10, 15], ages=[1, 2, 3, 4, 5]))  # Output: 34


# Optimised version using Fenwick Tree (Binary Indexed Tree) to achieve O(n log n) time complexity

# TC: O(n log n) using Fenwick Tree (Binary Indexed Tree)
# SC: O(n)
class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:

        # Step 1: Age aur Score ke hisab se sort karo
        players = sorted(zip(ages, scores))

        # Max score dhoondho taaki Fenwick tree ki size decide ho sake
        max_score = max(scores)

        # Fenwick Tree (Binary Indexed Tree) to store max sum for each score
        # Index represent karta hai score ko, value represent karti hai max team score ko
        bit = [0] * (max_score + 1)

        def update(score, val):
            # Tree mein upar jaate hue max value update karo
            idx = score
            while idx <= max_score:
                bit[idx] = max(bit[idx], val)
                idx += idx & (-idx)

        def query(score):
            # 0 se lekar 'score' tak ka maximum sum dhoondho
            max_val = 0
            idx = score
            while idx > 0:
                max_val = max(max_val, bit[idx])
                idx -= idx & (-idx)
            return max_val

        # Step 2: Har player ke liye O(log N) mein best sum dhoondho
        for _, score in players:
            # Pichle saare valid scores (jo <= current score hain) unka max nikalon
            current_best = query(score) + score
            # Is naye score aur sum ke saath tree ko update karo
            update(score, current_best)

        return query(max_score)


print(Solution().bestTeamScore(scores=[4, 5, 6, 5], ages=[2, 1, 2, 1]))  # Output: 16
print(Solution().bestTeamScore(scores=[1, 3, 5, 10, 15], ages=[1, 2, 3, 4, 5]))  # Output: 34