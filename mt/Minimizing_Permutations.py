"""

Minimizing Permutations

In this problem, you are given an integer N, and a permutation, P of the integers from 1 to N, denoted as (a_1, a_2, ..., a_N). You want to rearrange the elements of the permutation into increasing order, repeatedly making the following operation:
Select a sub-portion of the permutation, (a_i, ..., a_j), and reverse its order.
Your goal is to compute the minimum number of such operations required to return the permutation to increasing order.

Signature
int minOperations(int[] arr)

Input
Array arr is a permutation of all integers from 1 to N, N is between 1 and 8

Output
An integer denoting the minimum number of operations required to arrange the permutation in increasing order

Example
If N = 3, and P = (3, 1, 2), we can do the following operations:

Select (1, 2) and reverse it: P = (3, 2, 1).
Select (3, 2, 1) and reverse it: P = (1, 2, 3).

output = 2

"""

from collections import deque


def minOperations(arr):
    N = len(arr)
    target = tuple(range(1, N + 1))
    start = tuple(arr)

    # Edge case: if already sorted
    if start == target:
        return 0

    # Initialize the queue for BFS
    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        current, depth = queue.popleft()

        # Explore all possible reversals
        for i in range(N):
            for j in range(i + 1, N):
                # Reverse the subarray from i to j
                next_state = list(current)
                next_state[i : j + 1] = reversed(next_state[i : j + 1])
                next_state = tuple(next_state)

                # Check if we reached the target
                if next_state == target:
                    return depth + 1

                # If not visited, add to the queue
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, depth + 1))

    return -1  # Should never reach here if input is a valid permutation


# Example usage:
arr = [3, 1, 2]
print(minOperations(arr))  # Output: 2
