# https://cses.fi/problemset/task/1635/

'''
Feature              | CSES (Coin Combinations I)                  | LeetCode (Coin Change II)
---------------------|---------------------------------------------|-------------------------------------------
Type                 | Permutations (क्रम महत्वपूर्ण है)              | Combinations (क्रम महत्वपूर्ण नहीं है)
Example {1,2} for 3 | {1,1,1}, {1,2}, {2,1} (3 ways)              | {1,1,1}, {1,2} (2 ways)
Loop Order           | Outer: Target, Inner: Coins                 | Outer: Coins, Inner: Target
'''

# Note: Coin Combinations II is similar to Leetcode coin change II.

'''
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, x;
    cin >> n >> x;

    vector<int> coins(n);
    for (int i = 0; i < n; i++) cin >> coins[i];

    const int MOD = 1e9 + 7;
    vector<int> dp(x + 1, 0);

    dp[0] = 1;

    for (int i = 1; i <= x; i++) {
        for (int c : coins) {
            if (i - c >= 0) {
                dp[i] = (dp[i] + dp[i - c]) % MOD;
            }
        }
    }

    cout << dp[x] << "\n";
    return 0;
}
'''

def solve():
    # n = number of coins, x = target amount
    n, x = map(int, input().split())
    coins = list(map(int, input().split()))

    MOD = 10**9 + 7
    dp = [0] * (x + 1)
    dp[0] = 1

    for i in range(1, x + 1): # Target pe loop, pehle target fix karte hain
        for c in coins: # Har coin pe loop, har target ke liye har coin try karte hain
            if i - c >= 0:
                dp[i] = (dp[i] + dp[i - c]) % MOD

    print(dp[x])


# https://cses.fi/problemset/task/1634/

'''
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, x;
    cin >> n >> x;

    vector<int> coins(n);
    for (int i = 0; i < n; i++)
        cin >> coins[i];

    const int INF = 1e9;
    vector<int> dp(x + 1, INF);

    dp[0] = 0;

    for (int i = 1; i <= x; i++)
    {
        for (int c : coins)
        {
            if (i - c >= 0)
            {
                dp[i] = min(dp[i], dp[i - c] + 1);
            }
        }
    }

    if (dp[x] == INF)
        cout << -1 << "\n";
    else
        cout << dp[x] << "\n";

    return 0;
}
'''

def solve():
    # n = number of coins, x = target amount
    n, x = map(int, input().split())
    coins = list(map(int, input().split()))

    MOD = 10**9 + 7
    dp = [float('inf')] * (x + 1)
    dp[0] = 0

    for i in range(1, x + 1): # Target pe loop, pehle target fix karte hain
        for c in coins: # Har coin pe loop, har target ke liye har coin try karte hain
            if i - c >= 0:
                dp[i] = min(dp[i], dp[i - c] + 1)

    print(dp[x] if dp[x] != float('inf') else -1)


# https://cses.fi/problemset/task/1636


'''
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, x;
    cin >> n >> x;

    vector<int> coins(n);
    for (int i = 0; i < n; i++) cin >> coins[i];

    const int MOD = 1e9 + 7;
    vector<int> dp(x + 1, 0);

    dp[0] = 1;

    for (int c : coins) {
        for (int i = c; i <= x; i++) {
            dp[i] = (dp[i] + dp[i - c]) % MOD;
        }
    }

    cout << dp[x] << "\n";
    return 0;
}
'''