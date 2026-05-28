# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/

class Solution:
    def minimumDistance(self, word: str) -> int:

        def get_dist(char_idx1, char_idx2):

            if char_idx1 == 26:
                return 0 # 26th index matlab finger bahar hai

            r1, c1 = char_idx1 // 6, char_idx1 % 6
            r2, c2 = char_idx2 // 6, char_idx2 % 6

            return abs(r1 - r2) + abs(c1 - c2)

        # dp[other_f] stores the min distance where one finger is at word[i-1]
        # and the other finger is at 'other_f'
        # Shuruat mein bahut badi value (infinity)
        dp = {26: 0} # 26 represents 'None' or 'Starting out'

        for i in range(len(word)):

            target = ord(word[i]) - ord('A')

            prev = ord(word[i - 1]) - ord('A') if i > 0 else 26

            new_dp = {}

            for other_f, dist in dp.items():

                # Option 1: Move finger from 'prev' to 'target'
                # Other finger stays at 'other_f'
                d1 = dist + get_dist(prev, target)
                if other_f not in new_dp or d1 < new_dp[other_f]:
                    new_dp[other_f] = d1

                # Option 2: Move finger from 'other_f' to 'target'
                # Other finger (prev) now becomes the 'other_f' for next step
                d2 = dist + get_dist(other_f, target)
                if prev not in new_dp or d2 < new_dp[prev]:
                    new_dp[prev] = d2

            dp = new_dp

        return min(dp.values())


print(Solution().minimumDistance("CAKE"))  # Output: 3
print(Solution().minimumDistance("HAPPY"))  # Output: 6