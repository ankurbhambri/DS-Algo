# https://atcoder.jp/contests/dp/tasks/dp_q


import sys

# Fast I/O
input = sys.stdin.read

def solve():
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    h = list(map(int, data[1:n+1]))
    a = list(map(int, data[n+1:]))

    # BIT array to store max beauty for heights
    # Size n+1 because BIT is 1-indexed
    bit = [0] * (n + 1)

    def update(idx, val):
        while idx <= n:
            if val > bit[idx]:
                bit[idx] = val
            else:
                # Agar naya value chota hai, toh update ki zarurat nahi
                # (Lekin is problem mein beauty hamesha add ho rahi hai)
                pass
            idx += idx & -idx

    def query(idx):
        res = 0
        while idx > 0:
            if bit[idx] > res:
                res = bit[idx]
            idx -= idx & -idx
        return res

    for i in range(n):
        height = h[i]
        beauty = a[i]
        
        # 1. Height 'height' se chote saare flowers ka max beauty find karo
        max_prev = query(height - 1)
        
        # 2. Current flower ko add karke nayi max beauty
        current_total = max_prev + beauty
        
        # 3. BIT ko update karo is height ke liye
        update(height, current_total)

    #  maximum value in the whole BIT
    print(query(n))

if __name__ == "__main__":
    solve()