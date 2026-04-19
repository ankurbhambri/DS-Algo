# Recursive approach of 01 knap-sack

# TC: O(2^N) where N is number of items
# SC: O(N) for recursive stack space
def knapSackRecursive(bag_cap, wt, val, N):

    def helper(N, cap):

        if N == 0 or cap == 0:
            return 0

        else:
            item_wt = wt[N - 1]  # current item weight
            item_val = val[N - 1]  # current item value

            if item_wt <= cap:  # if current item weight is lte to bag capacity

                # Now we have two choices take or skip current item

                # 1. add current item with it's val
                t1 = item_val + helper(N - 1, cap - item_wt)

                # 2. skip current item
                t2 = helper(N - 1, cap)

                return max(t1, t2)

            # In case current item weight is more that bag capacity, move to next item.
            return helper(N - 1, cap)

    return helper(N, bag_cap)


# Memoization
# TC: O(N * W)
# SC: O(N * W)
def knapSackCache(bag_cap, wt, val, N):
    memo = {}

    # two values are changing N and bag capacity
    def helper(N, cap):

        if N == 0 or cap == 0:
            return 0

        # if (M, cap) already in memo
        elif (N, cap) in memo:
            return memo[(N, cap)]

        else:

            item_wt = wt[N - 1]  # current item weight
            item_val = val[N - 1]  # current item value

            if item_wt <= cap:  # if current item weight is lte to bag capacity

                # there are two cases 1 take current item and add it's val or 2 skip current item
                t1 = item_val + helper(N - 1, cap - item_wt)  # 1. add current item with it's val

                t2 = helper(N - 1, cap)  # 2 or skip current item

                c = max(t1, t2)

            else:  # in case current item weight is more that bag capacity

                c = helper(N - 1, cap)

            memo[(N, cap)] = c
            return c

    return helper(N, bag_cap)


# Tabulation approach
# TC: O(N * W)
# SC: O(N * W) because of 2D dp array
def knapsackTabular(bag_cap, wt, val, N):

    dp = [[0] * (bag_cap + 1) for _ in range(N)]

    for i in range(N):

        for wt in range(bag_cap + 1):  # wt is cap

            item_wt = wt[i]
            item_val = val[i]

            if i == 0:
                dp[i][wt] = item_val if item_wt <= wt else 0

            else:

                if item_wt <= wt:

                    # take
                    c1 = item_val + dp[i - 1][wt - item_wt]  # i - 1 is N - 1

                    # skip
                    c2 = dp[i - 1][wt]

                    # max (take, skip)
                    dp[i][wt] = max(c1, c2)

                # skip if current item weight is more than bag capacity
                else:
                    dp[i][wt] = dp[i - 1][wt]

    return dp[N - 1][bag_cap]


# Space optimized
# TC: O(N * W)
# SC: O(W)


'''
- Forward loop me dp[w - wt] already current item se update ho jata hai, isliye same item multiple times use ho jata hai (Unbounded Knapsack behavior)

- Reverse loop ensure karta hai ki dp[w - wt] previous row ka hi value ho, isliye har item sirf ek baar use hota hai (0/1 Knapsack)
'''
def knapSack_optimised(val, wt, W):

    dp = [0] * (W + 1)

    for cv, cw in zip(val, wt):
        # We loop backwards from W to the current item's weight
        # This ensures we don't use the same item multiple times for the same capacity
        for w in range(W, cw - 1, -1):

            dp[w] = max(dp[w], dp[w - cw] + cv)

    return dp[W]


n = 3  # number of weights and values
bag_cap = 5
wt = [2, 1, 4]
val = [12, 10, 6]

print(knapSackRecursive(bag_cap, wt, val, n))
print(knapSackCache(bag_cap, wt, val, n))
print(knapsackTabular(bag_cap, wt, val, n))
print(knapSack_optimised(val, wt, bag_cap))