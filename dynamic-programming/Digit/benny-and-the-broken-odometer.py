# https://www.hackerearth.com/problem/algorithm/benny-and-the-broken-odometer/

# Broken odometer mein digits 0, 1, 2, 3 hi dikhte hain. Benny apni car se n km travel karta hai. Odometer par kitne baar digit '3' aayega?

def solve(x):

    if x < 0:
        return 0

    s = str(x)
    memo = {}

    def dp(pos, tight, found):

        if pos == len(s):
            return 1 if found else 0

        if (pos, tight, found) in memo:
            return memo[(pos, tight, found)]

        limit = int(s[pos]) if tight else 9

        ans = 0

        for d in range(limit + 1):

            new_found = found or (d == 3)
            new_tight = tight and (d == limit)

            ans += dp(pos + 1, new_tight, new_found)

        memo[(pos, tight, found)] = ans
        return ans

    return dp(0, True, False)


print(solve(5))  # 4
print(solve(14))  # 12