# https://leetcode.com/problems/make-array-strictly-increasing/


from bisect import bisect, bisect_right


class Solution:
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:

        memo = {}
        arr2.sort()
        
        def helper(i, prev):

            if i == len(arr1):
                return 0

            if (i, prev) in memo:
                return memo[(i, prev)]

            cost = float('inf')
            
            # If arr1[i] is already greater than prev, we can leave it be.
            if arr1[i] > prev:
                cost = helper(i + 1, arr1[i])

            # Find a replacement with the smallest value in arr2.
            idx = bisect.bisect_right(arr2, prev)
            
            # Replace arr1[i], with a cost of 1 operation.
            if idx < len(arr2):
                cost = min(cost, 1 + helper(i + 1, arr2[idx]))

            memo[(i, prev)] = cost
            return cost
        
        res = helper(0, -1)
        
        return res if res < float('inf') else -1


print(Solution().makeArrayIncreasing([1,5,3,6,7], [1,3,2,4]))
print(Solution().makeArrayIncreasing([1,5,3,6,7], [4,3,1]))


# Bottom-up DP

class Solution:
    def makeArrayIncreasing(self, arr1, arr2):

        arr2 = sorted(set(arr2))

        # dp[last_value] = minimum operations
        dp = {-1: 0}

        for num in arr1:

            tmp = {}

            for prev, ops in dp.items():

                # Option 1: keep current number
                if num > prev:
                    tmp[num] = min(tmp.get(num, float('inf')), ops)

                # Option 2: replace with smallest arr2 value > prev
                idx = bisect_right(arr2, prev)

                if idx < len(arr2):

                    nxt = arr2[idx]

                    tmp[nxt] = min(tmp.get(nxt, float('inf')), ops + 1)

            dp = tmp

            if not dp:
                return -1

        return min(dp.values())


print(Solution().makeArrayIncreasing([1,5,3,6,7], [4,3,1])) # -1
print(Solution().makeArrayIncreasing([1,5,3,6,7], [1,3,2,4])) # 1