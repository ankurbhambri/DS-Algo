# https://leetcode.com/problems/range-sum-query-mutable/


class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.n = len(nums)

        # Tree is 1-indexed, initialized to 0
        self.tree = [0] * (self.n + 1)

        # Build the tree in O(n)
        for i in range(self.n):
            self._add(i + 1, nums[i])

    def _add(self, i: int, delta: int):
        """Adds delta to the tree at index i."""
        while i <= self.n:
            self.tree[i] += delta
            # Move to the next responsible index
            i += i & -i

    def _query(self, i: int) -> int:
        """Returns the prefix sum from nums[0] to nums[i-1]."""
        total = 0
        while i > 0:
            total += self.tree[i]
            # Move to the parent index
            i -= i & -i
        return total

    def update(self, index: int, val: int) -> None:
        # Calculate the difference between the new value and old value
        delta = val - self.nums[index]
        self.nums[index] = val
        # Update the tree (converting 0-indexed to 1-indexed)
        self._add(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        # sum[left...right] = prefix_sum(right) - prefix_sum(left - 1)
        return self._query(right + 1) - self._query(left)


print(NumArray([1, 3, 5]).sumRange(0, 2))  # Output: 9
print(NumArray([1, 3, 5]).update(1, 2))  # Update index 1 to value 2


# Similar: https://cses.fi/problemset/task/1648


import sys

def solve():

    # Fast I/O to handle 200,000 queries efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    q = int(input_data[1])
    
    # Store initial values in a 1-indexed list for easy alignment with the tree
    # Pad with 0 at index 0
    nums = [0] + [int(x) for x in input_data[2 : 2 + n]]

    # Initialize Fenwick Tree array with 1-based indexing
    tree = [0] * (n + 1)
    
    def _add(i: int, delta: int):
        """Internal helper to add a change value to the Fenwick Tree."""
        while i <= n:
            tree[i] += delta
            i += i & -i
            
    def _query(i: int) -> int:
        """Internal helper to find the prefix sum from 1 up to index i."""
        total = 0
        while i > 0:
            total += tree[i]
            i -= i & -i
        return total

    # Build the initial Fenwick tree in O(n log n)
    for idx in range(1, n + 1):
        _add(idx, nums[idx])
        
    output = []
    ptr = 2 + n
    
    # Process queries using clear structural logic
    for _ in range(q):
        query_type = int(input_data[ptr])
        
        if query_type == 1:
            # Update query: 1 k u (Change value at position k to u)
            k = int(input_data[ptr + 1])
            u = int(input_data[ptr + 2])
            
            # Calculate the change (delta) between new value and old value
            delta = u - nums[k]
            nums[k] = u  # Keep our tracker array updated
            
            _add(k, delta)
            ptr += 3
            
        else:
            # Sum query: 2 a b (Find sum between range [a, b])
            a = int(input_data[ptr + 1])
            b = int(input_data[ptr + 2])
            
            # Sum[a...b] = prefix_sum(b) - prefix_sum(a - 1)
            result = _query(b) - _query(a - 1)
            output.append(str(result))
            ptr += 3
            
    # Print out all query responses separated by newlines
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == '__main__':
    solve()