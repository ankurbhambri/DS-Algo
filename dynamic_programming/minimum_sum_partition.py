def minDifferenceMemo(arr, n):
    sm = sum(arr)
    memo = {}

    def helper(N, p1, W):
        p2 = W - p1
        if N == 0:
            return p1 - p2
        elif (N, p1) in memo:
            return memo[(N, p1)]
        else:
            item = arr[N - 1]
            if p1 - item >= p2 + item:
                c1 = helper(N - 1, p1 - item, W)
                c2 = helper(N - 1, p1, W)
                c = min(c1, c2)
            else:
                c = helper(N - 1, p1, W)
            memo[(N, p1)] = c
            return c

    return helper(n, sm, sm)


print(minDifferenceMemo([1, 6, 11, 5], 4))
