# https://codeforces.com/problemset/problem/1036/C


def solve(x):

    memo = {}
    s = str(x)

    def dp(pos, tight, cnt):

        if cnt > 3:
            return 0
        
        if pos == len(s):
            return 1

        if (pos, tight, cnt) in memo:
            return memo[(pos, tight, cnt)]

        # agar tight true hai to restriction hai, toh hum sirf s[pos] tak hi ja sakte hain, warna 9 tak ja sakte hain
        limit = int(s[pos]) if tight else 9

        ans = 0

        for d in range(limit + 1):

            new_count = cnt + (d != 0)

            new_tight = tight and (d == limit)

            ans += dp(pos + 1, new_tight, new_count)


        memo[(pos, tight, cnt)] = ans
        return ans

    return dp(0, True, 0)


l, r = 1, 1000
print(solve(r) - solve(l - 1)) # 1000

l, r = 1024, 1024
print(solve(r) - solve(l - 1)) # 1

l, r = 65536, 65536
print(solve(r) - solve(l - 1)) # 0

l, r = 999999, 1000001
print(solve(r) - solve(l - 1)) # 2