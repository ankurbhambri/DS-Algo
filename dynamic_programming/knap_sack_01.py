# Recursive approach of knap-sack 01


def knapSackRecursive(bag_cap, item_wt, item_val, N):

    def helper(N, cap):

        if N == 0 or cap == 0:
            return 0

        else:

            curr_wt = item_wt[N - 1]  # current item weight
            curr_val = item_val[N - 1]  # current item value

            if curr_wt <= cap:  # if current item weight is lte to bag capacity

                # Now we have two choices 1 take it or 2 skip current item
                # 1. add current item with it's val
                t1 = curr_val + helper(N - 1, cap - curr_wt)
                # 2 or skip current item
                t2 = helper(N - 1, cap)

                return max(t1, t2)

            else:  # in case current item weight is more that bag capacity

                return helper(N - 1, cap)

    return helper(N, bag_cap)


# Bottom Up iterative or tabulation approach
# TC: O(N * W)
# Space: O(W)
def knapSack(val, wt, W):

    n = len(val)
    dp = [0] * (W + 1)
    for i in range(n):
        for w in range(W, 0, -1):
            cv, cw = val[i], wt[i]
            if cw <= w:
                dp[w] = max(dp[w], dp[w - cw] + cv)
    return dp[W]


# memoization approach for knap-sack


def knapSackCache(bag_cap, item_wt, item_val, N):
    memo = {}

    # two values are changing N and bag capacity
    def helper(N, cap):

        if N == 0 or cap == 0:
            return 0

        # if (M, cap) already in memo
        elif (N, cap) in memo:
            return memo[(N, cap)]

        else:

            curr_wt = item_wt[N - 1]  # current item weight
            curr_val = item_val[N - 1]  # current item value

            if curr_wt <= cap:  # if current item weight is lte to bag capacity

                # there are two cases 1 take current item and add it's val or 2 skip current item
                t1 = curr_val + helper(
                    N - 1, cap - curr_wt
                )  # 1. add current item with it's val
                t2 = helper(N - 1, cap)  # 2 or skip current item

                c = max(t1, t2)

            else:  # in case current item weight is more that bag capacity

                c = helper(N - 1, cap)

            memo[(N, cap)] = c
            return c

    return helper(N, bag_cap)


def knapsackTabular(bag_cap, item_wt, item_val, N):
    dp = [[0] * (bag_cap + 1) for _ in range(N)]
    for i in range(N):
        for j in range(bag_cap + 1):  # j is cap
            curr_wt = item_wt[i]
            curr_val = item_val[i]
            if i == 0:
                if curr_wt <= j:
                    dp[i][j] = curr_val
                else:
                    dp[i][j] = 0

            else:
                if curr_wt <= j:
                    c1 = curr_val + dp[i - 1][j - curr_wt]  # i - 1 is N - 1
                    c2 = dp[i - 1][j]
                    dp[i][j] = max(c1, c2)
                else:
                    dp[i][j] = dp[i - 1][j]
    return dp[N - 1][bag_cap]


# Driver code
if __name__ == "__main__":
    N = 3  # weights and values of N items
    item_val = [12, 10, 6]
    item_wt = [2, 1, 4]
    bag_cap = 5

    print(knapSack(item_val, item_wt, bag_cap))
    print(knapSackCache(bag_cap, item_wt, item_val, N))
    print(knapsackTabular(bag_cap, item_wt, item_val, N))
    print(knapSackRecursive(bag_cap, item_wt, item_val, N))
