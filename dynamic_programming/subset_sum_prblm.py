# 1 means possible to create subset whose sum ewauls to target and 0 means not possible


def subsetSumRecursive(N, arr, sum):

    def helper(n, sm):
        if sm == 0:
            return 1
        elif n == 0:
            return 0

        else:
            item = arr[n - 1]
            if item <= sm:
                c1 = helper(n - 1, sm - item)
                c2 = helper(n - 1, sm)
                return c1 or c2
            else:
                return helper(n - 1, sm)

    return helper(N, sum)


def subsetSumMemo(N, arr, sum):
    memo = {}
    arr.sort(reverse=True)

    def helper(n, sm):
        if sm == 0:
            return 1
        elif n == 0:
            return 0
        elif (n, sm) in memo:
            return memo[(n, sm)]
        else:
            item = arr[n - 1]
            if item <= sm:
                c1 = helper(n - 1, sm - item)
                c2 = helper(n - 1, sm)
                c = c1 or c2
            else:
                c = 0
            memo[(n, sm)] = c
            return c

    return helper(N, sum)


def subsetSumTabular(N, arr, W):
    dp = [[0] * (W + 1) for _ in range(N)]
    for i in range(N):
        for w in range(W + 1):  # W value is j
            item = arr[i]
            if i == 0:
                if w == 0 or item == w:
                    dp[i][w] = 1
            else:
                if item <= w:
                    dp[i][w] = dp[i - 1][w - item] or dp[i - 1][w]
                else:
                    dp[i][w] = dp[i - 1][w]

    return dp[N - 1][W]


if __name__ == "__main__":
    N = 6  # N items
    arr = [3, 34, 4, 12, 5, 2]
    sum = 9

    print(subsetSumRecursive(N, arr, sum))
    print(subsetSumRecursive(N, arr, sum))
    print(subsetSumTabular(N, arr, sum))
