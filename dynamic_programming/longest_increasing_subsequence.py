
def longestSubsequence_memo(arr, N):

    memo = {}
    def solve(n, last_index):
        if n == 0:
            return 0
        elif (n, last_index) in memo:
            return memo[(n, last_index)]
        else:
            if last_index == -1 or arr[n - 1] < arr[last_index]:
                c1 = 1 + solve(n - 1, n - 1)
                c2 = solve(n - 1, last_index)
                c = max(c1, c2)
            else:
                c = solve(n - 1, last_index)
            memo[(n, last_index)] = c
            return c
    return solve(N, -1)

    
def longestSubsequence_iterative(arr, N):
    dp = [0] * N
    dp[0] = 1
    for i in range(1, N):
        y = arr[i]
        j = i - 1
        mx = 0
        # left side traversal
        while j >= 0:
            if arr[j] < y:
                mx = max(mx, dp[j])
            j -= 1
        dp[i] = 1 + mx
    return max(dp)

print(longestSubsequence_memo([0,8,4,12,2,10,6,14,1,9,5, 13,3,11,7,15], 16))
print(longestSubsequence_iterative([0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15], 16))
