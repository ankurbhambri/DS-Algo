# with itertools
from itertools import combinations


def combination(arr, r):
    return list(combinations(arr, r))


# TIME COMPLEXITY: O(nCr) - binomial coefficient (number of ways to choose r elements from a set of 𝑛 n elements)
# SPACE COMPLEXITY: O(nCr) - binomial coefficient

# example
arr = [1, 2, 3, 4]
r = 2
print(combination(arr, r))  # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]


# Without itertools
def without_itertools(arr, r):
    res = []

    def generate_combination(arr, r, start, comb):
        if r == 0:
            res.append(comb[:])
            return

        for i in range(start, len(arr)):
            comb.append(arr[i])
            generate_combination(arr, r - 1, i + 1, comb)
            comb.pop()

    generate_combination(arr, r, 0, [])
    return res


# Time complexity: O(nCr) - binomial coefficient (number of ways to choose r elements from a set of 𝑛 n elements)
# Space complexity: O(nCr) - binomial coefficient

# example
arr = [1, 2, 3, 4]
r = 2
print(
    "without_itertools ", without_itertools(arr, r)
)  # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]


# when array is not given only n is given
def n_combination(n, k):
    res = []

    def backtrack(start, comb):

        if len(comb) == k:
            res.append(comb[:])
            return

        for i in range(start, n + 1):
            comb.append(i)
            backtrack(i + 1, comb)
            comb.pop()

    backtrack(1, [])
    return res


print("n combinations ", n_combination(4, 2))
