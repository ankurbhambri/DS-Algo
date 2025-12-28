# https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/

from math import ceil

class Solution:
    def minDamage(self, power: int, damage, health) -> int:

        enemies = []
        total_damage = 0

        # Prepare (time, damage)
        for d, h in zip(damage, health):
            time = ceil(h / power)   # ceil(h / power)
            enemies.append((d, time))
            total_damage += d

        # Sort by decreasing damage / time
        # Avoid floating point by cross multiplication
        enemies.sort(key=lambda x: (-x[0] / x[1]))

        ans = 0

        for d, t in enemies:
            ans += total_damage * t
            total_damage -= d

        return ans

print(Solution().minDamage(3, [4, 2, 1], [5, 2, 1]))