# https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(x):

            if x <= 0:
                return 0

            memo = {}

            s = str(x)

            def dfs(pos, tight, started, last2, last1):

                if pos == len(s):
                    return (1, 0)

                if (pos, tight, started, last2, last1) in memo:
                    return memo[(pos, tight, started, last2, last1)]

                limit = int(s[pos]) if tight else 9

                total_cnt = 0
                total_wavy = 0

                for d in range(limit + 1):

                    ntight = tight and (d == limit)

                    # still leading zeros
                    if not started and d == 0:

                        cnt, wav = dfs(pos + 1, ntight, False, -1, -1)

                        total_cnt += cnt
                        total_wavy += wav

                    else:
                        # started hone ke baad, ab humare paas last2, last1, d hai, jiske basis pe hum waviness calculate kar sakte hain
                        if not started:

                            cnt, wav = dfs(pos + 1, ntight, True, -1, d)

                            total_cnt += cnt
                            total_wavy += wav

                        else:

                            sm = 0

                            # we already have at least 2 digits
                            if last2 != -1:

                                # to ek naya peak/valley mila.
                                if (
                                    (last1 > last2 and last1 > d) or
                                    (last1 < last2 and last1 < d)
                                ):
                                    sm = 1

                            new_last2 = last1
                            new_last1 = d

                            cnt, wav = dfs(pos + 1, ntight, True, new_last2, new_last1)

                            total_cnt += cnt

                            # yha hum, last2, last1, d ke basis pe sm kar rahe hain, kyunki yeh waviness ka contribution hai
                            total_wavy += wav + sm * cnt


                memo[(pos, tight, started, last2, last1)] = (total_cnt, total_wavy)

                return (total_cnt, total_wavy)

            return dfs(0, True, False, -1, -1)[1]

        return solve(num2) - solve(num1 - 1)


print(Solution().totalWaviness(1, 100))
print(Solution().totalWaviness(1, 1000))