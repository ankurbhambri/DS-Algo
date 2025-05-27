# number of subset can be drived from array


def perfect_sum_recursive(arr, W):

    def helper(n, W):
        if n == 0:
            if W == 0:
                return 1
            return 0
        else:
            item = arr[n - 1]
            if item <= W:
                c1 = helper(n - 1, W - item)
                c2 = helper(n - 1, W)
                return c1 + c2
            else:
                return helper(n - 1, W)

    return helper(len(arr), W)


def perfect_sum_memo(arr, W):
    memo = {}
    mod = 10**9 + 7
    arr.sort(reverse=True)

    def helper(N, sm):
        if N == 0:
            if sm == 0:
                return 1
            return 0
        elif (N, sm) in memo:
            return memo[(N, sm)]
        else:
            item = arr[N - 1]
            if item <= sm:
                c1 = helper(N - 1, sm - item)
                c2 = helper(N - 1, sm)
                c = (c1 + c2) % mod
            else:
                if sm == 0:
                    c = 1
                else:
                    c = 0
            memo[(N, sm)] = c
            return c

    return helper(len(arr), W)


def perfect_sum_tabular(arr, W):

    n = len(arr)
    mod = 10**9 + 7
    dp = [[0] * (W + 1) for _ in range(n)]

    for i in range(n):
        for j in range(W + 1):
            sm = j
            item = arr[i]
            if i == 0:
                if sm == 0:
                    if item == 0:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 1
                else:
                    if sm == item:
                        dp[i][j] = 1

            else:
                if item <= sm:
                    dp[i][j] = (dp[i - 1][sm - item] + dp[i - 1][sm]) % mod
                else:
                    dp[i][j] = dp[i - 1][sm]

    return dp[n - 1][W]


if __name__ == "__main__":

    arr = [9, 7, 0, 3, 9, 8, 6, 5, 7, 6]
    print(perfect_sum_recursive(arr, 31))
    print(perfect_sum_memo(arr, 31))
    print(perfect_sum_tabular(arr, 31))
