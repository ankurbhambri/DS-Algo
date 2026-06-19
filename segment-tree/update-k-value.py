'''
    You are given:
    - Array arr of size n 
    - q queries
        - Each query: (l, r, k)

    For each query:
    - Update all elements from index l to r to value k

    n -> 10^5
    queries -> 10^5

    Two variations :
    1) if k remains same
    2) if k is different
'''

# Case 1: When K remain the same, we can use a difference array technique to perform range updates.

# TC: O(n + q) for processing all queries and updating the array
# SC: O(n) for the difference array

def update_array(arr, queries, k):

    n = len(arr)

    diff = [0] * (n + 1)

    for l, r in queries:
        diff[l] += 1

        if r + 1 < n:
            diff[r + 1] -= 1

    coverage = 0

    for i in range(n):

        coverage += diff[i]

        if coverage > 0:
            arr[i] = k

    return arr


k = 10
arr = [1, 2, 3, 4, 5, 6]
queries = [(1, 3),(2, 5)]

print(update_array(arr, queries, k))

# Case 2: When K is different, we can use a segment tree with lazy propagation to perform range updates and queries efficiently.