# https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1

# Given an array of positive integers arr[] and a value sum, determine if there is a subset of arr[] with sum equal to given sum


# TC: O(2^n) where n is the number of elements in the array.
# SC: O(n) for the recursion stack.
class Solution:
    def isSubsetSum(self, arr, target_sum):
        n = len(arr)
        # 2D DP table ko -1 se initialize karenge. Size: n x (target_sum + 1)
        # dp[ind][target] store karega ki 'ind' tak ke elements se 'target' sum banana possible hai ya nahi
        memo = {}

        def solve(ind, target):
            # Base Case 1: Agar target 0 ho gaya, matlab hume subset mil gaya
            if target == 0:
                return True

            # Base Case 2: Agar hum pehle element (index 0) par hain
            if ind == 0:
                return arr[0] == target

            # Agar yeh state pehle se calculated hai, toh wahi se return kar do
            if (ind, target) in memo:
                return memo[(ind, target)]

            # Case 1: Not Pick (current element ko nahi le rahe)
            not_pick = solve(ind - 1, target)

            # Case 2: Pick (current element ko le rahe hain, agar wo target se chota ya barabar ho)
            pick = False
            if target >= arr[ind]:
                pick = solve(ind - 1, target - arr[ind])

            # Dono cases mein se agar ek bhi True de de, toh answer True hoga
            memo[(ind, target)] = not_pick or pick

            return memo[(ind, target)]

        # Last index (n-1) se start karenge aur target_sum tak dhundenge
        return solve(n - 1, target_sum)


print(Solution().isSubsetSum([3, 34, 4, 12, 5, 2], 9))  # Output: True


# TC: O(n * target_sum) where n is the number of elements in the array and target_sum is the target sum.
# SC: O(n * target_sum) for the dp array of size n x (target_sum + 1).
class Solution:
    def isSubsetSum(self, arr, target_sum):

        n = len(arr)
        # 2D DP table jisme saari values shuruat mein False hongi
        dp = [[False for _ in range(target_sum + 1)] for _ in range(n)]

        # Base Case 1: Kisi bhi index ke liye, agar target 0 hai toh answer hamesha True hoga
        for i in range(n):
            dp[i][0] = True

        # Base Case 2: Pehle element (index 0) ke liye, agar wo target_sum se chota hai,
        # toh sirf wahi ek sum (`arr[0]`) banana possible hai
        if arr[0] <= target_sum:
            dp[0][arr[0]] = True

        # Nested loops se baki table fill karenge
        for ind in range(1, n):
            for target in range(1, target_sum + 1):

                # Case 1: Not Pick (pichle row ki same column ki value uthayenge)
                not_pick = dp[ind - 1][target]

                # Case 2: Pick (pichle row mein se `target - arr[ind]` wali column check karenge)
                pick = False
                if target >= arr[ind]:
                    pick = dp[ind - 1][target - arr[ind]]

                # Dono ka OR le kar current cell mein store karenge
                dp[ind][target] = not_pick or pick

        # Final answer aakhri cell mein milega
        return dp[n - 1][target_sum]


print(Solution().isSubsetSum([3, 34, 4, 12, 5, 2], 9))  # Output: True


# TC: O(n * target_sum) where n is the number of elements in the array and target_sum is the target sum.
# SC: O(target_sum) for the dp array of size target_sum + 1.
class Solution:
    def isSubsetSum (self, arr, target_sum):
        # Ek 1D array banayenge boolean values ka, jiska size target_sum + 1 hoga.
        # dp[j] true hoga agar sum 'j' banaya ja sakta hai.
        dp = [False] * (target_sum + 1)

        # Base Case: 0 sum hamesha possible hai (empty subset se)
        dp[0] = True

        # Array ke har number ke liye check karenge
        for num in arr:
            # Piche se loop chalayenge takti ek hi number bar-bar use na ho
            for j in range(target_sum, num - 1, -1):
                # Agar pehle se j sum possible tha, ya fir (j - num) sum possible tha,
                # toh ab 'j' sum bhi possible ho jayega.
                dp[j] = dp[j] or dp[j - num]

        # Final answer dp[target_sum] mein store hoga
        return dp[target_sum]


print(Solution().isSubsetSum([3, 34, 4, 12, 5, 2], 9))  # Output: True