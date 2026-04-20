# https://cses.fi/problemset/task/1633/

# Top-down DP + memoization

# Tc: O(n), Sc: O(n)

import sys
sys.setrecursionlimit(10**7)

MOD = 10**9 + 7

n = int(input())
dp = [-1] * (n + 1)

def solve(x):

    if x == 0:
        return 1

    if x < 0:
        return 0

    if dp[x] != -1:
        return dp[x]

    ans = 0
    for i in range(1, 7):
        ans = (ans + solve(x - i)) % MOD

    dp[x] = ans
    return ans

print(solve(n))


# Bottom-up DP

# TC: O(n * 6) ≈ O(n)
# SC: O(n)

# recurrence relation: dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4] + dp[i-5] + dp[i-6]

MOD = 10**9 + 7

n = int(input())
dp = [0] * (n + 1)

dp[0] = 1

for i in range(1, n + 1):
    # dice 6 faces
    for j in range(1, 7):
        if i - j >= 0:
            dp[i] = (dp[i] + dp[i - j]) % MOD

print(dp[n])

'''
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    const int MOD = 1e9 + 7;
    vector<int> dp(n + 1, 0);

    dp[0] = 1;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= 6; j++) {
            if (i - j >= 0) {
                dp[i] = (dp[i] + dp[i - j]) % MOD;
            }
        }
    }

    cout << dp[n] << "\n";
    return 0;
}

'''