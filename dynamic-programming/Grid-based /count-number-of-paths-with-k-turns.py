# https://www.geeksforgeeks.org/count-number-of-paths-with-k-turns/

'''
    Given a "m x n" matrix, count number of paths to reach bottom right from top left with maximum k turns allowed. What is a turn? 
    A movement is considered turn, if we were moving along row and now move along column. OR we were moving along column and now move along row.
'''

# Recurrence

# Time Complexity: O(m * n * k)
# Space Complexity: O(m * n * k) for memoization
def count_paths_with_k_turns(m, n, k):

    memo = {}

    def count_paths(i, j, k, dir):

        if i == m-1 and j == n-1:
            return 1

        if i >= m or j >= n or k < 0:
            return 0

        if (i, j, k, dir) in memo:
            return memo[(i, j, k, dir)]

        # Whichever if or else we enter, the answer will come from that block only, and then will assign to the memo. This is beind decided at the first calling time of recursive function.
        if dir == 'right':
            # move right: same direction
            # move down: change direction → k - 1
            ans = count_paths(i, j+1, k, 'right') + count_paths(i+1, j, k-1, 'down')

        elif dir == 'down':
            # move down: same direction
            # move right: change direction → k - 1
            ans = count_paths(i+1, j, k, 'down') + count_paths(i, j+1, k-1, 'right')

        memo[(i, j, k, dir)] = ans

        return ans

    return count_paths(0, 0, k, 'right') + count_paths(0, 0, k, 'down')


print(count_paths_with_k_turns(3, 3, 1))  # Output: 6
print(count_paths_with_k_turns(3, 3, 2))  # Output: 12
print(count_paths_with_k_turns(3, 3, 0))  # Output: 2


