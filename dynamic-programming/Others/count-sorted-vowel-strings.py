# https://leetcode.com/problems/count-sorted-vowel-strings/


# TC: O(n)
# SC: O(1)
class Solution:
    def countVowelStrings(self, n: int) -> int:

        # Shuru mein n = 1 ke liye saare vowels ke paas 1 option hai

        # Index represent: [a, e, i, o, u]
        dp = [1, 1, 1, 1, 1]

        # Hum 2 se lekar n tak loop chalayenge
        for _ in range(2, n + 1):

            # Peeche se sum karte hue aayenge
            # Kyunki 'e' ka dependency 'i', 'o', 'u' par hai
            for i in range(3, -1, -1):
                dp[i] += dp[i + 1]

        return sum(dp)


print(Solution().countVowelStrings(1))  # Output: 5
print(Solution().countVowelStrings(2))  # Output: 15