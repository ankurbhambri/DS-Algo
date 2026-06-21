# https://leetcode.com/problems/integer-break/


'''
Maximum Product by Splitting Integer (Your "Multiply Instead of Plus" Question)

Given a natural number n, split it into positive integers that sum to n, and find the maximum possible product you can get from the split. 

If not splitting gives a larger number, return the number itself.

1	1 = 1
2	1 + 1, MAX(2, 1 * 1) = 2
3	1 + 1 + 1, 2 + 1, MAX(3, 1 * 1 * 1, 2 * 1) = 3
4	1 + 1 + 1 + 1, 2 + 2, 3 + 1, MAX(4, 1 * 1 * 1 * 1, 2 * 2, 3 * 1) = 4
5	1 + 1 + 1 + 1 + 1, 2 + 3, 4 + 1, MAX(5, 1 * 1 * 1 * 1 * 1, 2 * 3, 4 * 1) = 6
6	1 + 1 + 1 + 1 + 1 + 1, 2 + 4, 3 + 3, 5 + 1, MAX(6, 1 * 1 * 1 * 1 * 1 * 1, 2 * 4, 3 * 3, 5 * 1) = 9
7	1 + 1 + 1 + 1 + 1 + 1 + 1, 2 + 5, 3 + 4, 6 + 1, MAX(7, 1 * 1 * 1 * 1 * 1 * 1 * 1, 2 * 5, 3 * 4, 6 * 1) = 12
8	1 + 1 + 1 + 1 + 1 + 1 + 1 + 1, 2 + 6, 3 + 5, 4 + 4, 7 + 1, MAX(8, 1 * 1 * 1 * 1 * 1 * 1 * 1 * 1, 2 * 6, 3 * 5, 4 * 4, 7 * 1) = 18
9	1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1, 2 + 7, 3 + 6, 4 + 5, 8 + 1, MAX(9, 1 * 1 * 1 * 1 * 1 * 1 * 1 * 1 * 1, 2 * 7, 3 * 6, 4 * 5, 8 * 1) = 27

'''
        #  5
    #    /   \
#   (2 * 3)   2 * dp(3)

class Solution:
    def integerBreak(self, n: int) -> int:

        dp = [0] * (n + 1)

        dp[1] = 1 # 1 ko break nahi kar sakte rules ke hisab se, but logic ke liye 1 rakhte hain

        # first loop 2 se start hoga kyunki 1 ke liye break nahi kar sakte
        for i in range(2, n + 1):

            # second loop 1 se start hoga aur i-1 tak chalega kyunki hum i ko break kar rahe hain, aur break karne ke liye kam se kam 1 chahiye
            for j in range(1, i):

                # pehla option ye hai ki hum i ko j aur (i-j) me break karte hain aur unka product lete hain,
                option1 = j * (i - j)

                # aur dusra option ye hai ki hum i ko j aur dp[i-j] me break karte hain, 
                # jisme dp[i-j] ka matlab hai ki hum (i-j) ko aur break kar sakte hain aur uska maximum product le sakte hain.
                option2 = j * dp[i - j]

                dp[i] = max(dp[i], option1, option2)

        return dp[n]


print(Solution().integerBreak(8))   # Output: 18, because 8 can be split into 3 + 3 + 2, and 3 * 3 * 2 = 18
print(Solution().integerBreak(10))  # Output: 36, because 10 can be split into 3 + 3 + 4, and 3 * 3 * 4 = 36