# https://leetcode.com/problems/car-pooling/

class Solution:
    def carPooling(self, trips, capacity: int) -> bool:

        delta = []

        for p, u, v in trips:
            delta.append((u, p))
            delta.append((v, -p))

        for _, p in sorted(delta):
            capacity -= p
            if capacity < 0:
                return False
        return True

print(Solution().carPooling([[2, 1, 5], [3, 3, 7]], 4))  # False
print(Solution().carPooling([[2, 1, 5], [3, 3, 7]], 5))  # True
