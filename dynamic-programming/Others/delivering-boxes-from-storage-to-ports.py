# https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/


class Solution:
    def boxDelivering(self, boxes: list[list[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:

        n = len(boxes)
        dp = [0] * (n + 1)

        l = 0
        trips = 2 # Base cost: 1 to go out, 1 to come back
        current_weight = 0

        for r in range(n):

            current_weight += boxes[r][1]

            # If this box goes to a different port than the previous one, 
            # it adds an extra port-to-port trip.
            if r > 0 and boxes[r][0] != boxes[r - 1][0]:
                trips += 1

            # Shrink the window from the left if constraints are broken or if keeping the left box gives no advantage.
            while (
                r - l + 1 > maxBoxes or
                current_weight > maxWeight or
                (l < r and dp[l] == dp[l + 1])
            ):

                current_weight -= boxes[l][1]
                if boxes[l][0] != boxes[l + 1][0]:
                    trips -= 1 # Solved a port transition, reduce trip count
                l += 1

            # The best way to deliver up to box 'r'
            dp[r + 1] = dp[l] + trips

        return dp[n]


print(Solution().boxDelivering([[1,1],[2,1],[1,1]], 2, 3, 3)) # Output: 4
print(Solution().boxDelivering([[1,2],[3,3],[3,1],[3,1],[2,4]], 3, 3, 6)) # Output: 6