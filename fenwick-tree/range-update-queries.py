# https://cses.fi/problemset/task/1651

import sys
 

def solve():

    # Read all input from standard input at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # Parse n (size of array) and q (number of queries)
    n = int(input_data[0])
    q = int(input_data[1])

    # Parse the initial array arr (1-indexed for convenience)
    # We pad with a 0 at the beginning to match 1-based indexing
    arr = [0] + [int(i) for i in input_data[2 : 2 + n]]

    ######### Ignore: Above is the input parsing part, below is the Fenwick Tree implementation #########

    # The Fenwick Tree array (1-indexed, size n + 2 to handle b + 1 safely)
    tree = [0] * (n + 2)
    
    def add(i: int, delta: int):
        """Standard Fenwick Tree update: adds delta to tree at index i"""
        while i <= n:
            tree[i] += delta
            i += i & -i
            
    def query(i: int) -> int:
        """Standard Fenwick Tree query: returns prefix sum from 1 to i"""
        total = 0
        while i > 0:
            total += tree[i]
            i -= i & -i
        return total
 
    # Build the initial Fenwick tree using the differences of the original array
    for i in range(1, n + 1):
        difference = arr[i] - arr[i - 1]
        add(i, difference)
        
    # Process queries
    idx = 2 + n
    output = []
    
    for _ in range(q):
        type_of_query = int(input_data[idx])
        
        if type_of_query == 1:
            # Range update: Type 1 a b u
            a = int(input_data[idx + 1])
            b = int(input_data[idx + 2])
            u = int(input_data[idx + 3])
            
            add(a, u)       # Increase difference at the start boundary
            add(b + 1, -u)  # Cancel out the increase past the end boundary
            idx += 4
            
        else:
            # Point query: Type 2 k
            k = int(input_data[idx + 1])
            
            # The value at k is the prefix sum of differences
            actual_value = query(k)
            output.append(str(actual_value))
            idx += 2
            
    # Print all answers separated by newlines
    sys.stdout.write("\n".join(output) + "\n")
 
if __name__ == '__main__':
    solve()