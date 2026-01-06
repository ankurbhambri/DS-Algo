# https://leetcode.com/problems/painting-a-grid-with-three-different-colors/

# only difference is here the column is 3 and rows are <= 5k in above its vice versa, but logic remains same
# Similar = https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid


'''
Sabse pehle sabhi patterns generate kar lo jo ho sake agar row kam h toh first column ke liye pattern generate ho gyi agar column kam h toh first row ke pattern generate karlo logic dono ka same h

Then patterns ko adj se connect kar lo and then har pattern to 1 way dedo intially 

Uske baad dp mein row wise agar row jayada h else column wise start karo fill karna

Pehle OG dp se pattern, cost nikalo sabhi adj mein uski cost daal do simple and last mein swap and sum (dp.values)
'''


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:

        MOD = 10 ** 9 + 7

        # 1. Saare valid vertical patterns (masks) dhoondo
        valid_masks = []
        def generate_masks(current_mask):

            if len(current_mask) == m: # yha pe column/row ki value jo kam h
                valid_masks.append(tuple(current_mask))
                return

            for color in range(3):
                if not current_mask or current_mask[-1] != color:
                    generate_masks(current_mask + [color])

        generate_masks([])

        # 2. Pre-calculate karo ki kaunse do masks padosi ho sakte hain
        adj = {mask: [] for mask in valid_masks}
        for m1 in valid_masks:
            for m2 in valid_masks:
                if all(m1[i] != m2[i] for i in range(m)):
                    adj[m1].append(m2)

        # 3. DP initialization (Pehla column)
        dp = {mask: 1 for mask in valid_masks}

        # 4. Baaki n-1 columns/rows ke liye loop
        for _ in range(n - 1):
            new_dp = {mask: 0 for mask in valid_masks}
            # OG DP
            for mask, count in dp.items():
                # adj DP
                for next_mask in adj[mask]:
                    new_dp[next_mask] = (new_dp[next_mask] + count) % MOD

            dp = new_dp

        return sum(dp.values()) % MOD

print(Solution().colorTheGrid(1, 1))  # 3
print(Solution().colorTheGrid(1, 2))  # 6
print(Solution().colorTheGrid(5, 5))  # 580986