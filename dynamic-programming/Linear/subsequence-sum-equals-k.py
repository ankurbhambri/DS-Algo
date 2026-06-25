# TC: O(n * K)
# SC: O(n * K)
def count_subseq(arr, k):
    n = len(arr)

    memo = {}

    def dfs(i, curr_sum):
        if i == n:
            return 1 if curr_sum == k else 0

        if (i, curr_sum) in memo:
            return memo[(i, curr_sum)]

        take = dfs(i + 1, curr_sum + arr[i])
        not_take = dfs(i + 1, curr_sum)

        memo[(i, curr_sum)] = take + not_take
        return memo[(i, curr_sum)]

    return dfs(0, 0)


# TC: O(n * K)
# SC: O(K)
def count_subseq(arr, k):
    dp = [0] * (k + 1)
    dp[0] = 1

    for num in arr:
        for s in range(k, num - 1, -1):
            dp[s] += dp[s - num]

    return dp[k]