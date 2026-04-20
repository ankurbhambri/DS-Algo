# https://cses.fi/problemset/task/1637


'''
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> dp(n + 1, 1e9);
    dp[0] = 0;

    for (int i = 1; i <= n; i++) {

        int num = i;

        while (num > 0) {

            int digit = num % 10;


            if (digit > 0) {
                dp[i] = min(dp[i], dp[i - digit] + 1);
            }
            num /= 10;
        }
    }

    cout << dp[n] << endl;
}
'''

# TC: O(n log n), here log n is the number of digits in n, which is at most 6 for n <= 10^6
# SC: O(n), we are using a dp array of size n + 1

def solve():

    n = int(input())

    dp = [float('inf')] * (n + 1)

    dp[0] = 0

    for i in range(1, n + 1):

        num = i

        while num > 0:

            d = num % 10
            num //= 10

            if d > 0:
                dp[i] = min(dp[i], dp[i - d] + 1)

    print(dp[n])

if __name__ == "__main__":
    solve()