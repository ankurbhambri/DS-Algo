# https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

# TC: O(log n)
# SC: O(log n)
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(x):

            if x <= 0:
                return 0

            memo = {}
            s = str(x)

            def dfs(pos, tight, started, last2, last1):

                # count, waviness
                if pos == len(s):
                    return 1, 0

                state = (pos, tight, started, last2, last1)

                if state in memo:
                    return memo[state]

                limit = int(s[pos]) if tight else 9

                total_cnt = 0
                total_wavy = 0

                for d in range(limit + 1):

                    ntight = tight and (d == limit)

                    nstarted = started or (d != 0)

                    nlast2 = last1 if nstarted else last2
                    nlast1 = d if nstarted else -1

                    cnt, wav = dfs(pos + 1, ntight, nstarted, nlast2, nlast1)

                    total_cnt += cnt
                    total_wavy += wav

                    if nstarted and last2 >= 0 and last1 >= 0:
                        if (
                            (last2 < last1 and last1 > d)
                            or
                            (last2 > last1 and last1 < d)
                        ):
                            total_wavy += cnt

                memo[state] = (total_cnt, total_wavy)

                return memo[state]

            return dfs(0, True, False, -1, -1)[1]

        return solve(num2) - solve(num1 - 1)


print(Solution().totalWaviness(1, 100))
print(Solution().totalWaviness(1, 1000))