# https://leetcode.com/problems/ways-to-make-a-fair-array/


class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:

        res = 0
        n = len(nums)

        even_presum = [0] * (n + 1)
        odd_presum = [0] * (n + 1)

        for i, num in enumerate(nums):

            if i % 2: # odd not equal to 0
                odd_presum[i + 1] = odd_presum[i] + num
                even_presum[i + 1] = even_presum[i]

            else:
                even_presum[i + 1] = even_presum[i] + num
                odd_presum[i + 1] = odd_presum[i]

        for i in range(1, n + 1):

            odd_sum1 = odd_presum[i - 1] # left side of odd
            even_sum1 = even_presum[i - 1] # left side of even

            # even_presum[-1] and odd_presum[-1] is like total presum which is stored at last index

            # here we are trying removing each element and checking whether it is giving fair array or not

            # we need right side or odd and even and shift makes even to odd and odd to even so taking vice versa

            odd_sum2 = even_presum[-1] - even_presum[i] # when we remove a ith even value, values from right become odd
            even_sum2 = odd_presum[-1] - odd_presum[i] # same when we remove odd ith index value, other right side value become even

            # left side + right side for both presum array(odd, even)
            if odd_sum1 + odd_sum2 == even_sum1 + even_sum2:
                res += 1

        return res


print(Solution().waysToMakeFair([1, 1, 1]))
print(Solution().waysToMakeFair([2, 1, 6, 4]))