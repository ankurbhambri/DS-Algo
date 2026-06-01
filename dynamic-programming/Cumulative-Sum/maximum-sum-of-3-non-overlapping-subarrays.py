# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/

class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:

        n = len(nums)

        # Step 1: Har index se shuru hone wali k-size window ka sum nikalna
        # sums[i] matlab nums[i] se lekar nums[i+k-1] tak ka sum
        window_sum = 0
        sums = []
        for i in range(n):
            window_sum += nums[i]
            if i >= k:
                window_sum -= nums[i - k]
            if i >= k - 1:
                sums.append(window_sum)

        # sums array ki length ab (n - k + 1) ho chuki hai
        m = len(sums)

        # Step 2: left_max array banana (Left to Right)
        # left_max[i] store karega sums[0...i] tak ki best window ka starting index
        left_max = [0] * m
        best_idx = 0
        for i in range(m):
            if sums[i] > sums[best_idx]:
                best_idx = i
            left_max[i] = best_idx

        # Step 3: right_max array banana (Right to Left)
        # right_max[i] store karega sums[i...m-1] tak ki best window ka starting index
        right_max = [0] * m
        best_idx = m - 1
        for i in range(m - 1, -1, -1):
            # >= isliye lagaya taaki agar sum equal ho toh lexicographically chhota index mile
            if sums[i] >= sums[best_idx]:
                best_idx = i
            right_max[i] = best_idx

        # Step 4: Middle window ko fix karke maximum sum dhoondhna
        max_total = -1
        ans = []

        # Middle window 'i' kahan se kahan tak ja sakti hai?
        # Uske left mein kam se kam ek window (size k) aur right mein ek window (size k) honi chahiye
        for i in range(k, m - k):
            l_idx = left_max[i - k] # Left ki best window ka index
            r_idx = right_max[i + k] # Right ki best window ka index

            total = sums[l_idx] + sums[i] + sums[r_idx]

            if total > max_total:
                max_total = total
                ans = [l_idx, i, r_idx]

        return ans