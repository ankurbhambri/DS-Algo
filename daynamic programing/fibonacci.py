def fib(n, dp): # memoization recursive method
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if n not in dp:
        dp[n] = fib(n - 1, dp) + fib(n - 2, dp)
    return dp[n]


def fib_tab(n): # tabular approach
    tb = [0, 1]
    for i in range(2, n + 1):
        tb.append(tb[i - 1] + tb[i - 2])
    return tb[n]


dp = {0: 0, 1: 1, 2: 1}
print(fib(7, dp))
print(fib_tab(7))
