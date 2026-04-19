# https://atcoder.jp/contests/dp/tasks/dp_d

import sys

input_data = sys.stdin.read().split()

N = int(input_data[0])
W = int(input_data[1])

wt, val = [], []

pointer = 2
for _ in range(N):
    wt.append(int(input_data[pointer]))
    val.append(int(input_data[pointer + 1]))
    pointer += 2

# dp[w] stores the maximum value for a knapsack of capacity w
dp = [0] * (W + 1)

items = list(zip(wt, val))

for cw, cv in items:
    # We loop backwards from W to the current item's weight
    # This ensures we don't use the same item multiple times for the same capacity
    for w in range(W, cw - 1, -1):
        # Since the loop range already ensures cw <= w, 
        # the if condition is implicitly handled by the range boundary.
        dp[w] = max(dp[w], dp[w - cw] + cv)

print(dp[W])


# https://atcoder.jp/contests/dp/tasks/dp_e


import sys

def solve():

    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = 3 # int(input_data[0])
    W = 8 # int(input_data[1])

    items = []
    max_val = 0
    pointer = 2
    for _ in range(N):
        w = int(input_data[pointer])
        v = int(input_data[pointer + 1])
        items.append((w, v))
        max_val += v # Total possible value calculate kar rahe hain
        pointer += 2

    # Step 1 & 2: DP array for values, initialized to Infinity
    inf = float('inf')
    dp = [inf] * (max_val + 1)
    dp[0] = 0 

    # Step 3: Har item ke liye update karein
    for weight, value in items:
        # Reverse loop taaki ek item baar-baar na use ho
        for v in range(max_val, value - 1, -1):
            # Update dp[v] to be the minimum weight needed to achieve value v
            dp[v] = min(dp[v], dp[v - value] + weight)

    # Step 5: Answer nikalna
    # Humein wo sabse badi 'v' chahiye jiska weight W se kam ya barabar ho
    ans = 0
    for v in range(max_val, -1, -1):
        if dp[v] <= W:
            ans = v
            break

    print(ans)

if __name__ == "__main__":
    solve()