# https://leetcode.com/problems/maximum-height-by-stacking-cuboids/

class Solution:
    def maxHeight(self, cuboids: list[list[int]]) -> int:

        # pehle sort karlo har cuboid ke dimensions ko, taki unka order consistent ho
        for c in cuboids:
            c.sort()

         # then sort the cuboids themselves, so that we can apply a longest increasing subsequence type of approach
        cuboids.sort()

        n = len(cuboids)
        dp = [0] * n

        # yha pe hum longest increasing subsequence jaisa approach use karenge, 
        # jisme hum check karenge ki kya current cuboid ke dimensions previous cuboid ke dimensions se bade hain, agar haan to hum dp[i] ko update karenge
        for i in range(n):
            dp[i] = cuboids[i][2]
            for j in range(i):
                # check if cuboid j can be placed on top of cuboid i, which means all dimensions of j should be less than or equal to those of i
                if (cuboids[j][0] <= cuboids[i][0] and
                    cuboids[j][1] <= cuboids[i][1] and
                    cuboids[j][2] <= cuboids[i][2]
                ):
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])

        return max(dp)

print(Solution().maxHeight([[50,45,20],[95,37,53],[45,23,12]]))  # Output: 190