# ''' Bottom Up approach
#     Time Complexity: O(N*W)
#     Auxiliary Space: O(W) '''


# def knapSack(val, wt, W):
#     n = len(val)
#     dp = [0 for i in range(W + 1)]
#     for i in range(1, n + 1):
#         for w in range(W, 0, -1):
#             if wt[i - 1] <= w:
#                 dp[w] = max(dp[w], dp[w - wt[i - 1]] + val[i - 1])
#     return dp[W]


# # Driver code
# val = [12, 10, 6]
# wt = [2, 1, 4]
# W = 5

# print(knapSack(val, wt, W))

# # val = [359, 963, 465, 706, 146, 282, 828, 962, 492]
# # wt = [96, 43, 28, 37, 92, 5, 3, 54, 93]
# # W = 383
# # print(knapSack(val, wt, W))

def func(val, wt, cap, N):


    def solve(N, cap):

        if N == 0 or cap == 0:
            return 0
        
        else:

            curr_wt = wt[N - 1]
            curr_val = val[N - 1]

            if curr_wt <= curr_val:

                t1 = curr_val + solve(N - 1, cap - curr_wt) # 1
                t2 = solve(N - 1, cap) # 2

                return max(t1, t2)

            else:

                return solve(N - 1, cap)
    return solve(N, val)


N = 3 # weights and values of N items
val = [12, 10, 6]
wt = [2, 1, 4]
cap = 5

func(val, wt, cap, N)
